from .playing_piece import PlayingPiece


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]

    def add_piece(self, row: int, col: int, playing_piece: PlayingPiece):
        if self.board[row][col]:
            return False

        self.board[row][col] = playing_piece
        return True

    def get_free_cells(self):
        free_cells = []

        for row in range(self.size):
            for col in range(self.size):
                if not self.board[row][col]:
                    free_cells.append((row, col))

        return free_cells

    def print_board(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col]:
                    print(" " + self.board[row][col].piece_type.value, " ", end="")
                else:
                    print("    ", end="")

                print("|", end="")
            print()
