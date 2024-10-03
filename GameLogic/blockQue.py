import GameLogic.func as fc
from GameLogic.allBlocks import *


class BlockQue:
    def __init__(self):
        self.next_block = self.randomBlock()
        self.next_block.reset()

    def getNextBlock(self):
        return self.next_block

    def randomBlock(self):
        match fc.getRandomInt(6) + 1:
            case 1:
                return I_Block()
            case 2:
                return J_Block()
            case 3:
                return L_Block()
            case 4:
                return O_Block()
            case 5:
                return S_Block()
            case 6:
                return T_Block()
            case 7:
                return Z_Block()

    def getAndUpdate(self):
        tmp_block = self.next_block

        while True:
            self.next_block = self.randomBlock()
            if tmp_block.getID() != self.next_block.getID():
                break

        return tmp_block
