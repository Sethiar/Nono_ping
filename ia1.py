import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur_fenetre = 400
hauteur_fenetre = 300

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Paramètres de la raquette de l'IA
ia_raquette_largeur = 10
ia_raquette_hauteur = 60
ia_raquette_vitesse = 5

# Paramètres de la balle
balle_taille = 10
balle_vitesse_x = 5
balle_vitesse_y = 5

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu de Ping-Pong")

# Position initiale de la raquette de l'IA
ia_raquette_x = largeur_fenetre - ia_raquette_largeur
ia_raquette_y = hauteur_fenetre // 2 - ia_raquette_hauteur // 2

# Position initiale de la balle
balle_x = largeur_fenetre // 2 - balle_taille // 2
balle_y = hauteur_fenetre // 2 - balle_taille // 2
balle_direction_x = random.choice((1, -1))
balle_direction_y = random.choice((1, -1))

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mouvement de la balle
    balle_x += balle_vitesse_x * balle_direction_x
    balle_y += balle_vitesse_y * balle_direction_y

    # Mouvement de l'IA
    if balle_y > ia_raquette_y + ia_raquette_hauteur // 2:
        ia_raquette_y += ia_raquette_vitesse
    elif balle_y < ia_raquette_y + ia_raquette_hauteur // 2:
        ia_raquette_y -= ia_raquette_vitesse

    # Gestion des collisions avec les bords de l'écran
    if balle_y <= 0 or balle_y >= hauteur_fenetre - balle_taille:
        balle_direction_y *= -1

    # Gestion de la collision avec la raquette de l'IA
    if (balle_x + balle_taille >= ia_raquette_x and
            balle_y + balle_taille >= ia_raquette_y and
            balle_y <= ia_raquette_y + ia_raquette_hauteur):
        balle_direction_x *= -1

    # Effacement de l'écran
    fenetre.fill(blanc)

    # Dessin de la raquette de l'IA
    pygame.draw.rect(fenetre, noir, (ia_raquette_x, ia_raquette_y, ia_raquette_largeur, ia_raquette_hauteur))

    # Dessin de la balle
    pygame.draw.ellipse(fenetre, noir, (balle_x, balle_y, balle_taille, balle_taille))

    # Mise à jour de l'affichage
    pygame.display.flip()

# Fermeture de Pygame