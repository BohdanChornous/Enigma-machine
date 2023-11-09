import pygame
import string


class Reflector:

    def __init__(self, writing):
        self.left = string.ascii_uppercase
        self.right = writing

    def reflect(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def draw(self, screen, x, y, w, h, font):

        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "white", r, width=2, border_radius=15)

        # letters
        for i in range(26):

            # left hand side
            letter = self.left[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center=(x+w/4, y+((i+1)*h)/27))
            screen.blit(letter, text_box)

            # right hand side
            letter = self.right[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center=(x+w*3/4, y+((i+1)*h)/27))
            screen.blit(letter, text_box)
