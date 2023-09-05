import pygame
from pygame.locals import *

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre du jeu
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Vitesse de déplacement des raquettes
PADDLE_SPEED = 5

# Création de la fenêtre du jeu
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ping-Pong")

# Création des raquettes
paddle1 = pygame.Rect(10, WINDOW_HEIGHT / 2 - 50, 10, 100)
paddle2 = pygame.Rect(WINDOW_WIDTH - 20, WINDOW_HEIGHT / 2 - 50, 10, 100)

# Création de la balle
ball = pygame.Rect(WINDOW_WIDTH / 2 - 10, WINDOW_HEIGHT / 2 - 10, 20, 20)
ball_speed_x = 1
ball_speed_y = 1

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Déplacement des raquettes
    keys = pygame.key.get_pressed()
    if keys[K_UP] and paddle1.y > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[K_DOWN] and paddle1.y < WINDOW_HEIGHT - paddle1.height:
        paddle1.y += PADDLE_SPEED
    if keys[K_w] and paddle2.y > 0:
        paddle2.y -= PADDLE_SPEED
    if keys[K_s] and paddle2.y < WINDOW_HEIGHT - paddle2.height:
        paddle2.y += PADDLE_SPEED

    # Déplacement de la balle
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Rebond de la balle sur les bords supérieur et inférieur
    if ball.y > WINDOW_HEIGHT - 20 or ball.y < 0:
        ball_speed_y *= -1

    # Rebond de la balle sur les raquettes
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1

    # Effacement de l'écran
    window.fill(BLACK)

    # Affichage des raquettes et de la balle
    pygame.draw.rect(window, WHITE, paddle1)
    pygame.draw.rect(window, WHITE, paddle2)
    pygame.draw.ellipse(window, WHITE, ball)

    # Mise à jour de l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()