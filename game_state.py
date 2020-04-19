import itertools
from copy import deepcopy as dp


class GameState:
    EMPTY = "#"
    JMAX = "x"
    JMIN = "0"

    INITIAL_CONFIG = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

    def other_player(self):
        return GameState.JMIN if self.current_player == GameState.JMAX else GameState.JMAX

    def __str__(self):
        tmp = "player {} moves\n".format(self.current_player)
        if self.is_final():
            tmp = ""
        for line in self.config:
            tmp += " ".join(line) + "\n"
        return tmp

    def __init__(self, config=INITIAL_CONFIG, current_player=JMAX):
        self.config = config
        self.current_player = current_player

    def get_all_lines(self):
        return [x for x in self.config]

    def get_column(self, idx):
        return [row[idx] for row in self.config]

    def get_all_columns(self):
        return [self.get_column(i) for i in range(0, len(self.config))]

    def get_diagonals(self):
        return [[self.config[i][j]
                 for i in range(0, len(self.config))
                 for j in range(0, len(self.config[i]))
                 if i == j], [self.config[i][j]
                              for i in range(0, len(self.config))
                              for j in range(0, len(self.config[i]))
                              if i + 1 == len(self.config) - j]]

    def get_all(self):
        return list(itertools.chain(self.get_all_lines(), self.get_all_columns(), self.get_diagonals()))

    def is_full(self):
        return not any(x == GameState.EMPTY for line in self.config for x in line)

    def winner(self):
        winners = set(line[0] for line in self.get_all() if len(set(line)) == 1 and line[0] != GameState.EMPTY)
        winners = list(winners)
        if len(winners) == 1:
            return winners[0]
        else:
            return GameState.EMPTY

    def is_final(self):
        return self.winner() != GameState.EMPTY or self.is_full()

    def is_tie(self):
        return self.winner() == GameState.EMPTY and self.is_full()

    def score(self):
        if self.winner() == GameState.JMAX:
            return 1
        elif self.winner() == GameState.JMIN:
            return -1
        else:
            return 0

    def next_states(self):
        ans = []
        for i in range(0, len(self.config)):
            for j in range(0, len(self.config)):
                if self.config[i][j] == GameState.EMPTY:
                    nxt = dp(self.config)
                    nxt[i][j] = self.current_player
                    ans.append(GameState(nxt, self.other_player()))
        return ans



if __name__ == '__main__':
    state = GameState([["0", "x", "0"],
                       ["0", "x", "x"],
                       ["x", "0", "0"]], "x")
    print(state.is_tie())

    start_sate = GameState()
    for nxt in start_sate.next_states():
        print(nxt)
