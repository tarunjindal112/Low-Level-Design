from collections import deque
from model.board import Board
from model.player import Player
from model.playing_piece_X import PlayingPieceX
from model.playing_piece_O import PlayingPieceO
from model.piece_type import PieceType


class TicTacToeGame:
    players = deque()
    game_board: Board

    def initialize_board(self):
        cross_piece = PlayingPieceX()
        self.players.append(Player("Player1", cross_piece))
        noughts_piece = PlayingPieceO()
        self.players.append(Player("Player2", noughts_piece))
        self.game_board = Board(3)

    def start_game(self):
        no_winner = True
        while no_winner:
            player_turn = self.players.popleft()
            self.game_board.print_board()
            free_spaces = self.game_board.get_free_cells()
            if not free_spaces:
                no_winner = False
                continue

            print("Player:" + player_turn.name + " Enter row,column: ")
            s = input()
            row = int(s.split(",")[0])
            col = int(s.split(",")[1])

            piece_added_successfully = self.game_board.add_piece(row, col, player_turn.playing_piece)
            if not piece_added_successfully:
                print("Incorrect position chosen, try_again")
                self.players.appendleft(player_turn)
                continue
            self.players.append(player_turn)

            winner = self.is_there_winner(row, col, player_turn.playing_piece.piece_type)
            if winner:
                return player_turn.name

        return "tie"

    def is_there_winner(self, row, col, piece_type: PieceType):
        row_match = True
        col_match = True
        diagonal_match = True
        anti_diagonal_match = True
        size = self.game_board.size

        for i in range(size):
            if not self.game_board.board[row][i] or self.game_board.board[row][i].piece_type != piece_type:
                row_match = False

        for i in range(size):
            if not self.game_board.board[i][col] or self.game_board.board[i][col].piece_type != piece_type:
                col_match = False

        for i in range(size):
            if not self.game_board.board[i][i] or self.game_board.board[i][i].piece_type != piece_type:
                diagonal_match = False

        for i in range(size):
            if not self.game_board.board[i][size - i -1] or self.game_board.board[i][size - i -1].piece_type != piece_type:
                anti_diagonal_match = False

        return row_match or col_match or diagonal_match or anti_diagonal_match
