from.playing_piece import PlayingPiece


class Player:
    def __init__(self, name: str, playing_piece: PlayingPiece):
        self.name = name
        self.playing_piece = playing_piece

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_playing_piece(self):
        return self.playing_piece

    def set_playing_piece(self, playing_piece: PlayingPiece):
        self.playing_piece = playing_piece
