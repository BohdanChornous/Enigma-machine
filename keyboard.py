import pygame
import string


class Keyboard:

    def forward(self, letter) -> int:
        signal = string.ascii_uppercase.find(letter)
        return signal

    def backward(self, signal) -> str:
        letter = string.ascii_uppercase[signal]
        return letter

    def draw(self, screen, x, y, w, h, font):
        # rectangle
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "white", r, width=1, border_radius=7)

        # letters
        for i in range(26):
            letter = string.ascii_uppercase[i]
            letter = font.render(letter, True, 'grey')
            text_box = letter.get_rect(center=(x + w / 2, y + (i + 1) * h / 27))
            screen.blit(letter, text_box)

    def draw(self, screen, x, y, w, h, font):

        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "white", r, width=2, border_radius=15)

        for i in range(26):
            letter = string.ascii_uppercase[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center=(x+w/2, y+((i+1)*h)/27))
            screen.blit(letter, text_box)

