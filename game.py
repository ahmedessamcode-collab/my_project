import random
import pygame
pygame.init()


from snake import Snake
from items import *
from render import Render
from events import Events
from handlers import Handlers
from handle_screen import HandleScreen
import config


class Game:
    def __init__(self):
        self.width = config.WIDTH
        self.height = config.HEIGHT
        self.block_size = config.BLOCKSIZE
        self.initial_x = config.WIDTH // 2
        self.initial_y = config.HEIGHT // 2
        self.score = 0
        self.speed = config.SPEED
        self.running = False
        self.colors = config.COLORS

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")

        self.snake = Snake(self.initial_x, self.initial_y, self.block_size)
        self.food = Food(self.block_size, self.width, self.height, self.snake.snake_body)
        self.bonous = Bonous(self.block_size, self.width, self.height, self.snake.snake_body)
        self.bomb_ball = BoombBall(self.block_size, self.width, self.height, self.snake.snake_body)
        self.render = Render(self.screen)
        self.events = Events(self.snake, self.food, self.bomb_ball, self.bonous, self.height, self.width, self.block_size)
        self.handlers = Handlers(self.snake, self.bonous, self.bomb_ball)
        self.handle_screen = HandleScreen(self.width, self.height, self.colors, self.score, self.screen, self.render)

        self.random_mill_seconds_bonous = random.randint(30000, 38000)
        self.random_mill_seconds_bomb_ball = random.randint(22000, 27000)

        pygame.time.set_timer(self.handlers.BONUS_SPAWN_EVENT, self.random_mill_seconds_bonous)
        pygame.time.set_timer(self.handlers.BOMB_SPAWN_EVENT, self.random_mill_seconds_bomb_ball)

        self.lose_effect = pygame.mixer.Sound("you_lose.wav")
        self.got_point = pygame.mixer.Sound("got_point.wav")
        self.bonous_sound = pygame.mixer.Sound("bonous_sound.wav")
        self.speed_up = pygame.mixer.Sound("speed_up.wav")

    def run(self):
        if self.handle_screen.show_start_screen():
            self.running = True
        pygame.time.wait(1200)
        while self.running:
            if not self.handlers.running:
                self.running = False
            self.handlers.handle_actions()

            self.render.draw_background()
            self.snake.move()
            self.events.did_collide_screen()

            if self.events.did_collide_tail():
                self.lose_effect.play()
                self.running = False

            if self.events.did_eat_food():
                self.got_point.play()
                self.Increasing_scoreWithSpeed(1)
                self.food.position = self.food.create()

            elif self.handlers.bonus_visible and self.events.did_eat_bonous():
                self.bonous_sound.play()
                self.Increasing_scoreWithSpeed(3)
                self.handlers.bonus_visible = False

            elif self.handlers.bomb_visible and self.events.did_eat_bomb_ball():
                self.lose_effect.play()
                pygame.time.wait(1000)
                self.handlers.bomb_visible = False
                self.running = False
                

            else:
                self.snake.remove_tail()

            # Render every thing like sanke, food, score, bonous and bomb :-
            self.render.draw_snake(self.snake)
            self.render.draw_food(self.food)
            self.render.display_score(self.score, 20, 20, self.colors['white'])
            self.render.display_speed(self.speed, 20, 70, self.colors['green'])

            if self.handlers.bonus_visible:
                self.render.draw_bonous(self.bonous)

            if self.handlers.bomb_visible:
                self.render.draw_bomb_ball(self.bomb_ball)

        
            if not self.running:
                self.handle_screen = HandleScreen(self.width, self.height, self.colors, self.score, self.screen, self.render)
                pygame.time.wait(2000)
                if self.handle_screen.show_game_over_screen():
                    self.resetart_game()
                    self.running = True
                else:
                    break


            self.clock.tick(self.speed)
            pygame.display.flip()

        pygame.quit()


    def Increasing_scoreWithSpeed(self, increesing):
        self.score += increesing
        if self.score % 5 == 0 and self.score != 0:
            self.speed_up.play()
            self.speed += 1

    def resetart_game(self):
        self.snake = Snake(self.initial_x, self.initial_y, self.block_size)
        self.food = Food(self.block_size, self.width, self.height, self.snake.snake_body)
        self.bonous = Bonous(self.block_size, self.width, self.height, self.snake.snake_body)
        self.bomb_ball = BoombBall(self.block_size, self.width, self.height, self.snake.snake_body)
        self.score = 0
        self.speed = config.SPEED
        self.random_mill_seconds_bonous = random.randint(30000, 38000)
        self.random_mill_seconds_bomb_ball = random.randint(22000, 27000)
        pygame.time.set_timer(self.handlers.BONUS_SPAWN_EVENT, self.random_mill_seconds_bonous)
        pygame.time.set_timer(self.handlers.BOMB_SPAWN_EVENT, self.random_mill_seconds_bomb_ball)
        self.events = Events(self.snake, self.food, self.bomb_ball, self.bonous, self.height, self.width, self.block_size)
        self.handlers = Handlers(self.snake, self.bonous, self.bomb_ball)
