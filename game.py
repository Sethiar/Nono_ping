import pygame
from pygame.locals import *

class GameScreen:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.screen_color = (0, 0, 0)
        self.tool_color = (255, 255, 255)
        self.paddle_speed = 5
        self.clock = pygame.time.Clock()  # Créez un objet Clock

        self.create_paddle()
        self.create_ball()

    def create_paddle(self):
        self.paddle1 = pygame.Rect(10, 400 / 2 - 50, 10, 100)
        self.paddle2 = pygame.Rect(800 - 20, 400 / 2 - 50, 10, 100)

    def create_ball(self):
        self.ball = pygame.Rect(800 / 2 - 10,  400 / 2 - 10, 20, 20)
        self.ball_speed_x = 1
        self.ball_speed_y = 1


    def run_game(self):
        running = True
        FPS = 80
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Déplacement des raquettes
            keys = pygame.key.get_pressed()
            if keys[K_UP] and self.paddle1.y > 0:
                self.paddle1.y -= self.paddle_speed
            if keys[K_DOWN] and self.paddle1.y < 400 - self.paddle1.height:
                self.paddle1.y += self.paddle_speed
            if keys[K_w] and self.paddle2.y > 0:
                self.paddle2.y -= self.paddle_speed
            if keys[K_s] and self.paddle2.y < 400 - self.paddle2.height:
                self.paddle2.y += self.paddle_speed

            # Déplacement de la balle
            self.ball.x += self.ball_speed_x
            self.ball.y += self.ball_speed_y

            # Rebond de la balle sur les bords supérieur et inférieur
            if self.ball.y > 400 - 20 or self.ball.y < 0:
                self.ball_speed_y *= -1

            # Rebond de la ball sur les raquettes
            if self.ball.colliderect(self.paddle1) or self.ball.colliderect(self.paddle2):
                self.ball_speed_x *= -1

            # Affichage des raquettes et de la balle
            self.fenetre.fill(self.screen_color)
            pygame.draw.rect(self.fenetre, self.tool_color, self.paddle1)
            pygame.draw.rect(self.fenetre, self.tool_color, self.paddle2)
            pygame.draw.rect(self.fenetre, self.tool_color, self.ball)

            # Mise à jour de l'affichage
            pygame.display.flip()

            # Contrôlez le FPS en fonction de la vitesse souhaitée
            self.clock.tick(FPS)

        pygame.quit()

