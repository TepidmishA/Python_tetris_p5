from p5 import *
from GameLogic.constants import *


class TableShow:
    def __init__(self, grid_pos, text_show, size_t=Vector(4, 4), is_grid=0):
        self.back_color = 250
        self.size_t = size_t
        self.grid_pos = grid_pos
        self.text = text_show
        self.is_grid = is_grid
        self.block = None

    def update_block(self, block):
        self.block = block
        self.draw()

    def draw(self):
        pos = self.grid_pos

        push()

        # Draw field
        fill(self.back_color)
        stroke_weight(TABLE_BORDER_STROKE_WEIGHT)
        rect((pos.x * BLOCK_SIZE, pos.y * BLOCK_SIZE),
             self.size_t.x * BLOCK_SIZE, self.size_t.y * BLOCK_SIZE)

        # Draw grid
        if self.is_grid:
            stroke_weight(2)
            stroke(200)
            for x in range(int((pos.x + 1) * BLOCK_SIZE), int((pos.x + self.size_t.x) * BLOCK_SIZE), BLOCK_SIZE):
                for y in range(int((pos.y + 1) * BLOCK_SIZE), int((pos.y + self.size_t.y) * BLOCK_SIZE), BLOCK_SIZE):
                    line((x, pos.y * BLOCK_SIZE), (x, (pos.y + self.size_t.y) * BLOCK_SIZE))
                    line((pos.x * BLOCK_SIZE, y), ((pos.x + self.size_t.x) * BLOCK_SIZE, y))

            no_fill()
            stroke(0)
            rect((pos.x * BLOCK_SIZE, pos.y * BLOCK_SIZE),
                 self.size_t.x * BLOCK_SIZE, self.size_t.y * BLOCK_SIZE)

        pop()

        push()
        # Draw text
        if self.text:
            fill(TEXT_FILL)
            text_align('CENTER', 'BOTTOM')
            # text(self.text, (pos.x + self.size_t.x / 2) * BLOCK_SIZE, pos.y * BLOCK_SIZE - 5)
        pop()

        # Draw block
        if self.block:
            self.block.drawZeroOffset(self.grid_pos)
