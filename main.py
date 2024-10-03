from GameLogic.drawTable import TableShow
from GameLogic.gameState import GameState
from GameLogic.observers import *
from p5 import *
from GameLogic.constants import *

FONT = None
flag = True
game = None
controller = None


def setup():
    size(28 * BLOCK_SIZE, 24 * BLOCK_SIZE)
    background(CANVAS_COLOR)

    global FONT, game, controller

    FONT = create_font("Arial.ttf", 16, )
    text_font(FONT, TEXT_SIZE)
    fill(0)

    game = GameState()
    # controller = Controller(game)
    game.addObserver(HeldContainer())
    game.addObserver(NextContainer())
    game.addObserver(ShowField())


def start():
    global game
    game.start()


def draw():
    global flag
    if flag:
        flag = False
        start()


if __name__ == '__main__':
    run()
