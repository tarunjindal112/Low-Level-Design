from game.tic_tac_toe_game import TicTacToeGame


def main():
    game = TicTacToeGame()
    game.initialize_board()
    print("Game winner is: ", game.start_game())


if __name__ == "__main__":
    main()
