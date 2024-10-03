class Controller:
    def __init__(self, gameState):
        self.model = gameState

    def move(self, val):
        self.model.move(val)

    def start(self):
        self.model.start()

