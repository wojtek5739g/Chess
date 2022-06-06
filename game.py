import numpy as np

# class Piece:
#     def __init__(self, team, type, image, killable=False):
#         self.team = team
#         self.type = type
#         self.killable = killable
#         self.image = image

class GameState():
    def __init__(self):
        """
        Board of the game is 8x8 2d numpy array.
        Each element of the array has 2 characters.
        The first character represents color (different player) and the other - type of the piece
        "--" represents an empty location
        """
        self.board = np.array([
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        )
        self.whiteToMove = True
        self.moveLog = np.array([])

