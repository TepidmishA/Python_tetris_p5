from GameLogic.constants import *
import GameLogic.func as fc


class GameGrid:
    def __init__(self, rows, columns, offset):
        # displayed rows
        self.rows = rows
        self.columns = columns
        self.grid = []
        self.offset = offset

        for i in range(0, int(self.rows + EXTRA_ROWS)):
            self.grid.append([0 for _ in range(int(self.columns))])

    def draw(self):
        for r in range(EXTRA_ROWS, int(self.rows + EXTRA_ROWS)):
            for c in range(0, int(self.columns)):
                if self.get(r, c) != 0:
                    fc.drawCell(self.offset.x + c, self.offset.y + r - EXTRA_ROWS, self.get(r, c))

    '''if block spawns in block -> gameOver'''
    def checkGameOver(self, block):
        for elem in block.tilePositions():
            if self.get(elem.y, elem.x) != 0:
                return True

        return False

    def set(self, r, c, value):
        self.grid[int(r)][int(c)] = value

    def get(self, r, c):
        return self.grid[int(r)][int(c)]

    def isInside(self, r, c):
        return ((r >= 0) and (r < (self.rows + EXTRA_ROWS))
                and (c >= 0) and (c < self.columns))

    # change c / r --> r / c
    def isEmpty(self, c, r):
        return self.isInside(r, c) and self.get(r, c) == 0

    def isRowFull(self, r):
        for c in range(0, int(self.columns)):
            if self.get(r, c) == 0: return False
        return True

    def isRowEmpty(self, r):
        for c in range(0, int(self.columns)):
            if self.get(r, c) != 0: return False
        return True

    def clearRow(self, r):
        for c in range(0, int(self.columns)):
            self.set(r, c, 0)

    def moveRowDown(self, r, num_rows):
        for c in range(0, int(self.columns)):
            self.set(r + num_rows, c, self.get(r, c))
            self.set(r, c, 0)

    def clearFullRows(self):
        cleared = 0
        for r in range(int(self.rows - 1 + EXTRA_ROWS), -1, -1):
            if self.isRowFull(r):
                self.clearRow(r)
                cleared += 1
            elif cleared > 0:
                self.moveRowDown(r, cleared)

        return cleared
