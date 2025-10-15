import random

class Item:
    all_positions = []

    def __init__(self, block_size, width, height, snake_body):
        self.block_size = block_size
        self.width = width
        self.height = height
        self.snake_body = snake_body
        self.position = self.create()
        Item.all_positions.append(self.position)

    def create(self):
        while True:
            x = random.randint(0, (self.width - self.block_size) // self.block_size) * self.block_size
            y = random.randint(0, (self.height - self.block_size) // self.block_size) * self.block_size
            pos = (x, y)

            if pos not in self.snake_body and pos not in Item.all_positions:
                return pos


class Food(Item):
    pass


class Bonous(Item):
    pass


class BoombBall(Item):
    pass
