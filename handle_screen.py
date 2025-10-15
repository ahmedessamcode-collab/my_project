import pygame
from button import Button

class HandleScreen:
    def __init__(self, width, height, colors, score, screen, render):
        self.width = width
        self.height = height
        self.colors = colors
        self.score = score
        self.screen = screen
        self.render = render
        self.button_surface = pygame.image.load("button.png")
        self.button_surface = pygame.transform.scale(self.button_surface, (200, 100))
        self.button_font = pygame.font.SysFont("cambria", 40)

        self.restart_button = Button(
            image=self.button_surface,
            x_pos=self.width // 2,
            y_pos=self.height - 240,
            text_input="RESTART",
            font=self.button_font,
            base_color="white",
            hovering_color="green"
        )

        self.quit_button = Button(
            image=self.button_surface,
            x_pos=self.width // 2,
            y_pos=self.height - 100,
            text_input="QUIT",
            font=self.button_font,
            base_color="white",
            hovering_color="red"
        )
        
        self.mous_click = pygame.mixer.Sound("mous_click.wav")

    def show_start_screen(self):
        waiting = True
        while waiting:
            self.render.draw_starting_background()
            self.render.display_word("PREES ENTER TO START...", 200, self.height // 2, self.colors["black"])
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    pygame.quit()
                    return False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        start_sound = pygame.mixer.Sound("start_sound.wav")
                        start_sound.play()
                        waiting = False
                        return True

    def show_game_over_screen(self):
        waiting = True
        while waiting:
            self.render.draw_game_over()
            self.render.display_score(self.score, 552, 600, self.colors['black'])

            # Draw buttons
            self.restart_button.update(self.screen)
            self.restart_button.changeColor(pygame.mouse.get_pos())
            self.quit_button.update(self.screen)
            self.quit_button.changeColor(pygame.mouse.get_pos())

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mous_click.play()
                    if self.restart_button.rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.time.wait(500)
                        waiting = False
                        return True
                    elif self.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
                        pygame.time.wait(800)
                        waiting = False
                        return False