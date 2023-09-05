import pygame
from options import OptionScreen
from game import GameScreen

class MenuScreen:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.font = pygame.font.Font(None, 30)
        self.load_assets()
        self.setup_button()
        self.game_screen = GameScreen(fenetre)
        self.options_screen = OptionScreen(fenetre)

    def load_assets(self):
        self.background_menu = pygame.image.load("image/ping_pong2.jpg")
        self.background_menu = pygame.transform.scale(self.background_menu, (800, 400))

    def setup_button(self):
        self.button_play = pygame.Rect(20, 40, 150, 50)
        self.button_options = pygame.Rect(20, 90, 150, 50)
        self.button_quit = pygame.Rect(20, 140, 150, 50)

    def draw_buttons(self, rect, text, text_color=pygame.Color("black"), button_color=pygame.Color("gold")):
        pygame.draw.rect(self.fenetre, button_color, rect)
        pygame.draw.rect(self.fenetre, text_color, rect, 2)
        text_surface = self.font.render(text, True, text_color)
        text_position = (rect.left + 40, rect.top + 10)
        self.fenetre.blit(text_surface, text_position)

    def show(self):
        self.fenetre.blit(self.background_menu, (0, 0))
        self.draw_buttons(self.button_play, "Play")
        self.draw_buttons(self.button_options, "Options")
        self.draw_buttons(self.button_quit, "Quitter")

        # Ajouter un titre
        title_font = pygame.font.Font("font/static/Phudu-Bold.ttf", 48)
        title_text = title_font.render("Nono-Pong", True, pygame.Color("gold"))
        title_position = (self.fenetre.get_width()//2, 30)
        self.fenetre.blit(title_text, title_position)

    def handle_click(self, pos, current_screen, game_screen, options_screen):
        if self.button_play.collidepoint(pos):
            current_screen = game_screen
        elif self.button_options.collidepoint(pos):
            current_screen = options_screen
        elif self.button_quit.collidepoint(pos):
            pygame.quit()
            quit()
        return current_screen

    def run_menu(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.button_play.collidepoint(event.pos):
                        self.game_screen.run_game()
                        print("Play")

                    if self.button_options.collidepoint(event.pos):
                        self.options_screen.button_fonction()

                    if self.button_quit.collidepoint(event.pos):
                        pygame.quit()
                        running = False

            self.show()
            pygame.display.flip()
        pygame.quit()

