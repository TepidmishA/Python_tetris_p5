from GameLogic.block import Block
from p5 import Vector


class I_Block(Block):
    def __init__(self):
        tmp_tiles = [
            [Vector(0, 1), Vector(1, 1), Vector(2, 1), Vector(3, 1)],
            [Vector(2, 0), Vector(2, 1), Vector(2, 2), Vector(2, 3)],
            [Vector(0, 2), Vector(1, 2), Vector(2, 2), Vector(3, 2)],
            [Vector(1, 0), Vector(1, 1), Vector(1, 2), Vector(1, 3)]
        ]
        super().__init__(Vector(3, -2), 1, tmp_tiles)


class J_Block(Block):
    def __init__(self):
        tmp_tiles = [
            [Vector(0, 0), Vector(0, 1), Vector(1, 1), Vector(2, 1)],
            [Vector(1, 0), Vector(2, 0), Vector(1, 1), Vector(1, 2)],
            [Vector(0, 1), Vector(1, 1), Vector(2, 1), Vector(2, 2)],
            [Vector(1, 0), Vector(1, 1), Vector(0, 2), Vector(1, 2)]
        ]
        super().__init__(Vector(3, -1), 2, tmp_tiles)


class L_Block(Block):
    def __init__(self):
        tmp_tiles = [
            [Vector(2, 0), Vector(0, 1), Vector(1, 1), Vector(2, 1)],
            [Vector(1, 0), Vector(1, 1), Vector(1, 2), Vector(2, 2)],
            [Vector(0, 1), Vector(1, 1), Vector(2, 1), Vector(0, 2)],
            [Vector(0, 0), Vector(1, 0), Vector(1, 1), Vector(1, 2)]
        ]
        super().__init__(Vector(3, -1), 3, tmp_tiles)


class O_Block(Block):
    def __init__(self):
        tmp_tiles = [
            [Vector(0, 0), Vector(1, 0), Vector(0, 1), Vector(1, 1)],
            [Vector(0, 0), Vector(1, 0), Vector(0, 1), Vector(1, 1)],
            [Vector(0, 0), Vector(1, 0), Vector(0, 1), Vector(1, 1)],
            [Vector(0, 0), Vector(1, 0), Vector(0, 1), Vector(1, 1)]
        ]
        super().__init__(Vector(4, 0), 4, tmp_tiles)


class S_Block(Block):
    def __init__(self):
        tmp_tiles = [
            [Vector(1, 0), Vector(2, 0), Vector(0, 1), Vector(1, 1)],
            [Vector(1, 0), Vector(1, 1), Vector(2, 1), Vector(2, 2)],
            [Vector(1, 1), Vector(2, 1), Vector(0, 2), Vector(1, 2)],
            [Vector(0, 0), Vector(0, 1), Vector(1, 1), Vector(1, 2)]
        ]
        super().__init__(Vector(3, -1), 5, tmp_tiles)


class T_Block(Block):
    def __init__(self):
        tmp_tiles = [
            [Vector(1, 0), Vector(0, 1), Vector(1, 1), Vector(2, 1)],
            [Vector(1, 0), Vector(1, 1), Vector(2, 1), Vector(1, 2)],
            [Vector(0, 1), Vector(1, 1), Vector(2, 1), Vector(1, 2)],
            [Vector(1, 0), Vector(0, 1), Vector(1, 1), Vector(1, 2)]
        ]
        super().__init__(Vector(3, -1), 6, tmp_tiles)


class Z_Block(Block):
    def __init__(self):
        tmp_tiles = [
            [Vector(0, 0), Vector(1, 0), Vector(1, 1), Vector(2, 1)],
            [Vector(2, 0), Vector(1, 1), Vector(2, 1), Vector(1, 2)],
            [Vector(0, 1), Vector(1, 1), Vector(1, 2), Vector(2, 2)],
            [Vector(1, 0), Vector(0, 1), Vector(1, 1), Vector(0, 2)]
        ]
        super().__init__(Vector(3, -1), 7, tmp_tiles)
