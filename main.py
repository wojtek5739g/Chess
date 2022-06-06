import pygame
from pygame.locals import *
import game

DIM = 8
WIDTH = 800
HEIGHT = 800
MAX_FPS = 15 # for animation
IMAGES = {}

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

RECT_WIDTH = WIDTH/DIM

def load_images():
    """
        We can access an image by saying 'IMAGES['wp']'
    """
    pieces = ["bR", "bN", "bB", "bQ", "bK", "wR", "wN", "wB", "wQ", "wK", "bp", "wp"]
    for name in pieces:
        IMAGES[name] = pygame.transform.scale(pygame.image.load("images/" + name + ".png"), (RECT_WIDTH, RECT_WIDTH))


def main():
    pygame.init()

    clock = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    gameState = game.GameState()
    print(gameState.board)
    # print(gameState.board[0, :])
    # print(gameState.board[6, 5])
    load_images()

    DISPLAY.fill(WHITE)

    drawGameState(DISPLAY, gameState)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        clock.tick(MAX_FPS)
        pygame.display.update()

"""
    Responsible for graphics in a current game state.
"""

def drawGameState(screen, gameState):
    drawBoard(screen)
    drawPieces(screen, gameState.board)

"""
    Draw squares on the board
"""
def drawBoard(screen):
    for i in range(0, DIM):
        for j in range(0, DIM):
            if (i%2==0 and j%2!=0) or (i%2!=0 and j%2==0):
                pygame.draw.rect(screen, BLUE, (j*RECT_WIDTH, i*RECT_WIDTH, RECT_WIDTH, RECT_WIDTH))

"""
    Draw the pieces on the board using the current gameState.board
"""
def drawPieces(screen, board):
    for row in range(0, DIM):
        for col in range(0, DIM):
            if (board[row, col] == "--"):
                continue
            screen.blit(IMAGES[board[row, col]], pygame.Rect(col*RECT_WIDTH, row*RECT_WIDTH, RECT_WIDTH, RECT_WIDTH))


if __name__ == "__main__":
    main()