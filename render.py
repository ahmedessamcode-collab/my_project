import pygame
import config

class Render():
    def __init__(self, screen):
        self.screen = screen
        self.colors = config.COLORS
        self.block_size = config.BLOCKSIZE
        self.width = config.WIDTH
        self.height = config.HEIGHT
        self.font = pygame.font.Font(None, 60)


        self.background_image = pygame.image.load("background.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

        self.starting_background_image = pygame.image.load("starting_background.png")
        self.starting_background_image = pygame.transform.scale(self.starting_background_image, (self.width, self.height))

        self.game_over_image = pygame.image.load("game_over.png")
        self.game_over_image = pygame.transform.scale(self.game_over_image, (self.width, self.height))

        self.food_image = pygame.image.load("ball.png")
        self.food_image = pygame.transform.scale(self.food_image, (self.block_size, self.block_size))

        self.bonous_image = pygame.image.load("bonous.png")
        self.bonous_image = pygame.transform.scale(self.bonous_image, (self.block_size, self.block_size))
        
        self.bomb_ball_image = pygame.image.load("bomb_ball.png")
        self.bomb_ball_image = pygame.transform.scale(self.bomb_ball_image, (self.block_size, self.block_size))

        self.body_curve_1 = pygame.image.load("body_curvy1.png")
        self.body_curve_1 = pygame.transform.scale(self.body_curve_1, (self.block_size, self.block_size))


    def draw_background(self):
        self.screen.blit(self.background_image, (0, 0))


    def draw_starting_background(self):
        self.screen.blit(self.starting_background_image, (0, 0))


    def draw_snake(self, snake):
        head_img = snake.head_img
        if snake.direction == "up":
            head_img = pygame.transform.rotate(snake.head_img, 90)
        elif snake.direction == "down":
            head_img = pygame.transform.rotate(snake.head_img, -90)
        elif snake.direction == "left":
            head_img = pygame.transform.rotate(snake.head_img, 180)

        self.screen.blit(head_img, snake.snake_body[0])

        for i in range(1, len(snake.snake_body) - 1):
            x, y = snake.snake_body[i]
            prev_x, prev_y = snake.snake_body[i - 1]
            next_x, next_y = snake.snake_body[i + 1]

            if prev_x - x > self.width // 2:
                prev_x -= self.width
            elif x - prev_x > self.width // 2:
                prev_x += self.width

            if next_x - x > self.width // 2:
                next_x -= self.width
            elif x - next_x > self.width // 2:
                next_x += self.width

            if prev_y - y > self.height // 2:
                prev_y -= self.height
            elif y - prev_y > self.height // 2:
                prev_y += self.height

            if next_y - y > self.height // 2:
                next_y -= self.height
            elif y - next_y > self.height // 2:
                next_y += self.height

            body_img = snake.body_img

            if prev_x == next_x:
                rotated_body = pygame.transform.rotate(body_img, 90)
            elif prev_y == next_y:
                rotated_body = body_img
            else:
                if (prev_x < x and next_y < y) or (next_x < x and prev_y < y):
                    rotated_body = pygame.transform.rotate(self.body_curve_1, 180)
                elif (prev_y < y and next_x > x) or (next_y < y and prev_x > x):
                    rotated_body = pygame.transform.rotate(self.body_curve_1, 90)
                elif (prev_x > x and next_y > y) or (next_x > x and prev_y > y):
                    rotated_body = pygame.transform.rotate(self.body_curve_1, 0)
                elif (prev_y > y and next_x < x) or (next_y > y and prev_x < x):
                    rotated_body = pygame.transform.rotate(self.body_curve_1, 270)

            self.screen.blit(rotated_body, (x % self.width, y % self.height))


        if len(snake.snake_body) > 1:
            tail_dir = snake.get_tail_direction()
            tail_img = snake.tail_img
            if tail_dir == "up":
                tail_img = pygame.transform.rotate(snake.tail_img, 90)
            elif tail_dir == "down":
                tail_img = pygame.transform.rotate(snake.tail_img, -90)
            elif tail_dir == "left":
                tail_img = pygame.transform.rotate(snake.tail_img, 180)

            tx, ty = snake.snake_body[-1]
            self.screen.blit(tail_img, (tx % self.width, ty % self.height))


    def draw_food(self, food):
        self.screen.blit(self.food_image, (food.position[0], food.position[1]))


    def draw_bonous(self, bonous):
        self.screen.blit(self.bonous_image, (bonous.position[0], bonous.position[1]))


    def draw_bomb_ball(self, bomb_ball):
        self.screen.blit(self.bomb_ball_image, (bomb_ball.position[0], bomb_ball.position[1]))


    def display_score(self, score, x, y, color):
        text = self.font.render(f"Score: {score}", True, color)
        self.screen.blit(text, (x, y))


    def display_speed(self, speed, x, y, color):
        text = self.font.render(f"Speed: {speed}", True, color)
        self.screen.blit(text, (x, y))


    def display_word(self, world, x, y, color):
        text = self.font.render(f"{world}", True, color)
        self.screen.blit(text, (x, y))


    def draw_game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))
