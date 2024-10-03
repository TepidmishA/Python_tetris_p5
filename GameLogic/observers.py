from GameLogic.gameState import Observer
from GameLogic.drawTable import TableShow
from p5 import Vector
from GameLogic.constants import *


class HeldContainer(Observer):
    def __init__(self):
        super().__init__()
        self.container = TableShow(Vector(2, 2), "HELD")

    def evnt(self, model):
        self.container.update_block(model.getHeldBlock())


class NextContainer(Observer):
    def __init__(self):
        super().__init__()
        self.container = TableShow(Vector(22, 2), "NEXT")

    def evnt(self, model):
        self.container.update_block(model.getNextBlock())


class ShowField(Observer):
    def __init__(self):
        super().__init__()
        self.container = TableShow(FIELD_POS, None, Vector(10, 20), True)

    def evnt(self, model):
        self.container.draw()
        model.drawGame()
