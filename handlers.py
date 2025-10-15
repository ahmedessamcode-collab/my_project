import pygame
import random

class Handlers:
    def __init__(self, snake, bonous, bomb_ball):
        self.snake = snake
        self.bonous = bonous
        self.bomb_ball = bomb_ball
        self.BONUS_SPAWN_EVENT = pygame.USEREVENT + 1
        self.BONUS_HIDE_EVENT = pygame.USEREVENT + 2
        self.BOMB_SPAWN_EVENT = pygame.USEREVENT + 3
        self.BOMB_HIDE_EVENT = pygame.USEREVENT + 4
        self.bonus_visible = False
        self.bomb_visible = False
        self.running = True
        

    def handle_actions(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_keypress(event.key)

            # To create the bonous and hide it :
            elif event.type == self.BONUS_SPAWN_EVENT:
                self.bonous.position = self.bonous.create()
                self.bonus_visible = True
                pygame.time.set_timer(self.BONUS_HIDE_EVENT, 4000, loops=1)
                self.random_mill_seconds_bonous = random.randint(31000, 38000)
        

            elif event.type == self.BONUS_HIDE_EVENT:
                self.bonus_visible = False

            # To create the bomb ball & and hide it :
            elif event.type == self.BOMB_SPAWN_EVENT:
                self.bomb_ball.position = self.bomb_ball.create()
                self.bomb_visible = True
                pygame.time.set_timer(self.BOMB_HIDE_EVENT, 10000, loops=1)
                self.random_mill_seconds_bomb_ball = random.randint(22000, 27000)

            elif event.type == self.BOMB_HIDE_EVENT:
                self.bomb_visible = False

    def handle_keypress(self, key):
        if key == pygame.K_UP and self.snake.direction != "down":
            self.snake.direction = "up"
        elif key == pygame.K_DOWN and self.snake.direction != "up":
            self.snake.direction = "down"
        elif key == pygame.K_RIGHT and self.snake.direction != "left":
            self.snake.direction = "right"
        elif key == pygame.K_LEFT and self.snake.direction != "right":
            self.snake.direction = "left"