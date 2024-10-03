from abc import ABC, abstractmethod
from GameLogic.constants import *
from GameLogic.gameGrid import GameGrid
from GameLogic.blockQue import BlockQue
from GameLogic.exceptions import *
import logging
import math

import threading
import time
import keyboard


class Observer(ABC):
    @abstractmethod
    def evnt(self, model):
        pass


class GameState:
    def __init__(self, offset=FIELD_POS):
        self.field_offset = offset
        self.game_grid = GameGrid(FIELD_SIZE.y, FIELD_SIZE.x, self.field_offset)
        self.block_que = BlockQue()

        self.curr_block = self.block_que.getAndUpdate()
        self.held_block = None

        self.game_over = False

        self.all_obs = []
        self.interval_id = None

        self.is_running = False
        self.is_paused = False
        self.move_thread = None

        self.game_speed = GAMESPEED_MIN  # ms
        self.total_lines_cleared = 0
        self.score = 0
        self.level = 0

    def _update(self):
        for obs in self.all_obs:
            obs.evnt(self)

    def isGameOver(self): return self.game_over

    def getScore(self): return self.score
    def getLevel(self): return self.level
    def getLinesCleared(self): return self.total_lines_cleared
    def getGameSpeed(self): return self.game_speed

    def getCurrBLockPos(self):
        logging.info(f"Curr block y: {self.curr_block.getStartOffset().y} {self.curr_block.getCurrOffset().y}")

    def getNextBlock(self): return self.block_que.getNextBlock()
    def getHeldBlock(self): return self.held_block

    def setHeldBlock(self):
        self.held_block = self.curr_block
        self.held_block.reset()

    def addObserver(self, obs): self.all_obs.append(obs)

    def start(self):
        self._update()

        self.is_running = True
        self.is_paused = False
        self.move_thread = threading.Thread(target=self.startFalling)
        self.move_thread.start()

    def startFalling(self):
        time.sleep(1)
        while True:
            if self.is_running and not self.is_paused:
                self.move(83)
                time.sleep(self.game_speed / 1000)
            else:
                time.sleep(0.1)

    def drawGame(self):
        self.game_grid.draw()

        self.curr_block.drawShadow(self.field_offset, self.blockDropDistance())
        self.curr_block.draw(self.field_offset)

    def blockFits(self):
        for elem in self.curr_block.tilePositions():
            if not (self.game_grid.isEmpty(elem.x, elem.y)):
                return False

        return True

    def move(self, event):
        if event != 83:
            logging.info("GameState move:", event)

        match event:
            case 27:
                # alert('You stoped the game')
                pass
            case 69:
                self.rotateRight()
            case 81:
                self.rotateLeft()
            case 83:
                self.moveBlockDown()
            case 65:
                self.moveBlockLeft()
            case 68:
                self.moveBlockRight()
            case 32:
                self.hardDrop()
            case 9:
                self.switchHeldBlock()

        self._update()

    def rotateRight(self):
        self.curr_block.rotateRight()

        if not (self.blockFits()):
            self.curr_block.rotateLeft()

    def rotateLeft(self):
        self.curr_block.rotateLeft()

        if not (self.blockFits()):
            self.curr_block.rotateRight()

    def moveBlockLeft(self):
        self.curr_block.move(-1, 0)

        if not (self.blockFits()):
            self.curr_block.move(1, 0)

    def moveBlockRight(self):
        self.curr_block.move(1, 0)

        if not (self.blockFits()):
            self.curr_block.move(-1, 0)

    def placeBlock(self):
        if self.isGameOver():
            raise GameOver()
        else:
            logging.info("Block placed")

            # positions of cells in gameGrid matrix
            for elem in self.curr_block.tilePositions():
                self.game_grid.set(elem.y, elem.x, self.curr_block.getID())

            self.checkLevel(self.game_grid.clearFullRows())

            self.curr_block = self.block_que.getAndUpdate()
            self.game_over = self.game_grid.checkGameOver(self.curr_block)

    def moveBlockDown(self):
        self.curr_block.move(0, 1)

        if not (self.blockFits()):
            self.curr_block.move(0, -1)
            self.placeBlock()

    """Scoring system"""
    def addScore(self, lines):
        extra = 0
        match lines:
            case 1:
                extra =  40 * (self.level + 1)
            case 2:
                extra = 100 * (self.level + 1)
            case 3:
                extra = 300 * (self.level + 1)
            case 4:
                extra = 1200 * (self.level + 1)

        self.score += extra

    def checkLevel(self, lines):
        self.addScore(lines)

        tmp = self.total_lines_cleared + lines
        if int(math.floor(tmp / 10)) != self.level:
            self.game_speed = max(GAMESPEED_MAX, self.game_speed - GAMESPEED_DECREASE)

            """invoking function"""
            # clearInterval(this.intervalId);
            # this.intervalId = setInterval(() => this.move(83), this.gameSpeed);

        self.total_lines_cleared = tmp
        self.level = math.floor(tmp / 10)

    def tileDropDistance(self, pos):
        drop = 0

        while self.game_grid.isEmpty(pos.x, pos.y + drop + 1):
            drop += 1

        return drop

    def blockDropDistance(self):
        drop = self.game_grid.rows

        # positions of cells in gameGrid matrix
        for elem in self.curr_block.tilePositions():
            drop = min(drop, self.tileDropDistance(elem))

        return drop

    # change moveBlockDown to move n steps at once
    def hardDrop(self):
        tmp = self.blockDropDistance()
        if PLACE_BLOCK_AFTER_HARDDROP: tmp += 1

        for i in range(0, tmp):
            self.moveBlockDown()

    def switchHeldBlock(self):
        if self.held_block is None:
            self.setHeldBlock()
            self.curr_block = self.block_que.getAndUpdate()
        else:
            tmp = self.getHeldBlock()
            self.setHeldBlock()
            self.curr_block = tmp
