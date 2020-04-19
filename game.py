from game_state import GameState


class Game:
    MAX_DEPTH = 5

    def __init__(self, state):
        self.state = state

    def play(self):
        if self.state.current_player == GameState.JMAX:
            self.ai_move()
        else:
            self.player_move()

    def player_move(self):
        while True:
            try:
                print(game.state)
                inp = input("your move: ").split(" ")
                x = int(inp[0])
                y = int(inp[1])
                if self.state.config[x][y] != GameState.EMPTY:
                    raise ValueError("You're not allowed to move there")
                self.state.config[x][y] = self.state.current_player
                self.state.current_player = self.state.other_player()
                break
            except:
                print("Unable to move there, try again")

    def ai_move(self):
        self.state = min_max(self.state).picked_state

    def is_over(self):
        return self.state.is_final()

    def winner(self):
        return self.state.winner()


def min_max(state):
    if state.is_final():
        state.estimate = state.score()
        return state

    moves = state.next_states()
    scores = [min_max(move) for move in moves]

    if state.current_player == GameState.JMAX:
        state.picked_state = max(scores, key=lambda x: x.estimate)
    else:
        state.picked_state = min(scores, key=lambda x: x.estimate)
    state.estimate = state.picked_state.estimate
    return state


if __name__ == '__main__':
    game = Game(
        GameState([["x", "#", "#"],
                 ["#", "#", "#"],
                 ["#", "#", "#"]], current_player="0")
    )

    while not game.is_over():
        game.play()

    print("Game over")
    print("Winner is {}".format(game.winner()))
    print(game.state)
