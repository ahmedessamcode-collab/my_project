class Events:
    def __init__(self, snake, food, bomb_ball, bonous, height, width, block_size):
        self.snake = snake
        self.food = food
        self.bomb_ball = bomb_ball
        self.bonous = bonous
        self.height = height
        self.width = width
        self.block_size = block_size

    def did_eat_food(self):
        return self.snake.snake_body[0] == self.food.position

    def did_eat_bonous(self):
        return self.snake.snake_body[0] == self.bonous.position

    def did_eat_bomb_ball(self):
        return self.snake.snake_body[0] == self.bomb_ball.position

    def did_collide_tail(self):
        return self.snake.snake_body[0] in self.snake.snake_body[1:]

    def did_collide_screen(self):
        x, y = self.snake.snake_body[0]

        if x < 0:
            x = self.width - self.block_size
        elif x >= self.width:
            x = 0

        if y < 0:
            y = self.height - self.block_size
        elif y >= self.height:
            y = 0

        self.snake.snake_body[0] = (x, y)
        self.snake.head = self.snake.snake_body[0]