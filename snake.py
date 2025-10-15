import pygame

class Snake:
    def __init__(self, initial_x, initial_y, block_size):
        self.block_size = block_size
        self.snake_body = [
            (initial_x, initial_y),
            (initial_x - self.block_size, initial_y),
            (initial_x - 2 * self.block_size, initial_y)
        ]
        self.direction = "right"
        self.head = self.snake_body[0]

        self.head_img = pygame.image.load("head.png")
        self.head_img = pygame.transform.scale(self.head_img, (block_size, block_size))

        self.body_img = pygame.image.load("body.png")
        self.body_img = pygame.transform.scale(self.body_img, (block_size, block_size))

        self.tail_img = pygame.image.load("tail.png")
        self.tail_img = pygame.transform.scale(self.tail_img, (block_size, block_size))
        

    def move(self):
        if self.direction == "right":
            new_head = (self.head[0] + self.block_size, self.head[1])
        elif self.direction == 'left':
            new_head = (self.head[0] - self.block_size, self.head[1])
        elif self.direction == 'up':                                            
            new_head = (self.head[0], self.head[1] - self.block_size)
        elif self.direction == 'down':
            new_head = (self.head[0], self.head[1] + self.block_size)

        self.snake_body.insert(0, new_head)
        self.head = self.snake_body[0]
    
    def get_tail_direction(self):
        if len(self.snake_body) < 2:
            return "right"

        tail = self.snake_body[-1]
        before_tail = self.snake_body[-2]

        dx = tail[0] - before_tail[0]
        dy = tail[1] - before_tail[1]

        if dx > 0:
            return "right"
        elif dx < 0:
            return "left"
        elif dy > 0:
            return "down"
        elif dy < 0:
            return "up"
        return "right"
    
    def remove_tail(self):
        self.snake_body.pop()
