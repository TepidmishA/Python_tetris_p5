import random
from p5 import *
from GameLogic.constants import BLOCK_COLOR, SHADOW_COLOR, CELL_STROKE, BLOCK_SIZE


def getRandomInt(m):
    return random.randint(0, m)


def drawCell(x, y, ID, transp=False):
    push()

    pos = Vector(x, y)
    if transp:
        fill(SHADOW_COLOR[ID])
    else:
        fill(BLOCK_COLOR[ID])

    stroke_weight(CELL_STROKE)
    rect(pos.x * BLOCK_SIZE, pos.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

    pop()