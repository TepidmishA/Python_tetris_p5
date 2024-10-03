from p5 import Vector
from GameLogic.constants import *
import GameLogic.func as fc


"""Abstract class"""
class Block:
    def __init__(self, start_offset, ID, tiles):
        if type(self) is Block:
            raise TypeError("Object of Abstract Class cannot be created")

        self.rotation_state = None
        self.curr_offset = None

        # position of block in gameGrid matrix
        self.start_offset = Vector(start_offset.x, start_offset.y + EXTRA_ROWS)
        self.ID = ID
        self.tiles = tiles

        self.reset()

    def reset(self):
        self.rotation_state = 2
        self.curr_offset = self.start_offset.copy()

    # return positions of cells in gameGrid matrix
    def tilePositions(self):
        for elem in self.tiles[self.rotation_state]:
            yield Vector(elem.x + self.curr_offset.x, elem.y + self.curr_offset.y)

    def getID(self): return self.ID
    def getStartOffset(self): return self.start_offset
    def getCurrOffset(self): return self.curr_offset

    def draw(self, global_offset):
        for elem in self.tilePositions():
            if (elem.y - EXTRA_ROWS) >= 0:
                fc.drawCell(global_offset.x + elem.x, global_offset.y + elem.y - EXTRA_ROWS, self.ID)

    def drawShadow(self, global_offset, offset_y):
        for elem in self.tilePositions():
            fc.drawCell(global_offset.x + elem.x, global_offset.y + elem.y + offset_y - EXTRA_ROWS, self.ID, True)

    def drawZeroOffset(self, global_offset):
        for elem in self.tiles[self.rotation_state]:
            fc.drawCell(global_offset.x + elem.x, global_offset.y + elem.y, self.ID)

    def rotateRight(self):
        self.rotation_state = (self.rotation_state + 1) % len(self.tiles)

    def rotateLeft(self):
        if self.rotation_state == 0:
            self.rotation_state = len(self.tiles) - 1
        else:
            self.rotation_state -= 1

    def move(self, x, y):
        self.curr_offset.x += x
        self.curr_offset.y += y
