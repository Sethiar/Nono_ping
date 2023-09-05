import pygame

class OptionScreen:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.font = pygame.font.Font(None, 28)
        self.speed_frame_visible = False
        self.difficulty_frame_visible = False
        self.setup_button()
        self.setup_frame()

    def back(self):
        return "Retour"

    def setup_button(self):
        self.button_speed = pygame.Rect(20, 40, 200, 30)
        self.button_difficulty = pygame.Rect(20, 80, 200, 30)
        self.button_back = pygame.Rect(20, 120, 200, 30)

    def setup_frame(self):
        self.difficulty_frame = pygame.Rect(100, 180, 400, 50)
        self.difficulty_choice = [
            pygame.Rect(self.difficulty_frame.left + 10, self.difficulty_frame.top + 10, 120, 30),
            pygame.Rect(self.difficulty_frame.left + 130, self.difficulty_frame.top + 10, 120, 30),
            pygame.Rect(self.difficulty_frame.left + 250, self.difficulty_frame.top + 10, 120, 30)
        ]
        self.speed_frame = pygame.Rect(100, 250, 325, 50)
        self.speed_choice = [
            pygame.Rect(self.speed_frame.left + 25, self.speed_frame.top + 10, 50, 30),
            pygame.Rect(self.speed_frame.left + 100, self.speed_frame.top + 10, 50, 30),
            pygame.Rect(self.speed_frame.left + 175, self.speed_frame.top + 10, 50, 30),
            pygame.Rect(self.speed_frame.left + 250, self.speed_frame.top + 10, 50, 30)
        ]


    def draw_buttons(self, rect, text, text_color=pygame.Color("black"), button_color=pygame.Color("gold")):
        pygame.draw.rect(self.fenetre, button_color, rect)
        pygame.draw.rect(self.fenetre, pygame.Color("orange"), rect, 2)
        text_surface = self.font.render(text, True, text_color)
        text_position = (rect.left + 40, rect.top + 10)
        self.fenetre.blit(text_surface, text_position)

    def draw_frame(self, frame_rect, buttons, labels):
        pygame.draw.rect(self.fenetre, pygame.Color("black"), frame_rect)
        for i, button_rect in enumerate(buttons):
            pygame.draw.rect(self.fenetre, pygame.Color("darkgrey"), button_rect)
            pygame.draw.rect(self.fenetre, pygame.Color("black"), button_rect, 2)
            text_surface = self.font.render(labels[i], True, pygame.Color("black"))
            text_position = (button_rect.left + 10, button_rect.top + 5)
            self.fenetre.blit(text_surface, text_position)


    def show(self):
        self.draw_buttons(self.button_speed, "Speed")
        self.draw_buttons(self.button_difficulty, "Difficulty")
        self.draw_buttons(self.button_back, "Retour")
        if self.difficulty_frame_visible:
            self.draw_frame(self.difficulty_frame, self.difficulty_choice,
                            ["Facile", "Normale", "Extrême"])
        if self.speed_frame_visible:
            self.draw_frame(self.speed_frame, self.speed_choice,
                            ["1", "2", "3", "4"])

    def button_fonction(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.button_difficulty.collidepoint(event.pos):
                        self.difficulty_frame_visible = not self.difficulty_frame_visible
                        for i, button_rect in enumerate(self.difficulty_choice):
                            print("Difficulté :", ["Facile", "Normal", "Extrême"][i])

                    if self.button_speed.collidepoint(event.pos):
                        self.speed_frame_visible = not self.speed_frame_visible
                        for i, button_rect in enumerate(self.speed_choice):
                            print("Vitesse:", ["1", "2", "3", "4"][i])

                    if self.button_back.collidepoint(event.pos):
                        return self.back()

            self.fenetre.fill((150, 125, 25))
            self.show()
            pygame.display.flip()

