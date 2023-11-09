import pygame
import string


class Rotor:

    def __init__(self, writing, notch):
        self.left = string.ascii_uppercase
        self.right = writing
        self.notch = notch

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal

    def rotate(self, n=1, forward=True):
        for i in range(n):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[-1] + self.left[:-1]
                self.right = self.right[-1] + self.right[:-1]

    def rotate_to_letter(self, letter):
        n = string.ascii_uppercase.find(letter)
        self.rotate(n)

    def set_ring(self, position):

        # rotate the rotor backwards
        self.rotate(position-1, forward=False)

        # adjust the turnover notch in relationship to the wiring
        position_notch = string.ascii_uppercase.find(self.notch)
        self.notch = string.ascii_uppercase[(position_notch - position) % 26]

    def draw(self, screen, x, y, w, h, font):

        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, "white", r, width=2, border_radius=15)

        # letters
        for i in range(26):

            # left hand side
            letter = self.left[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center=(x+w/4, y+((i+1)*h)/27))

            # highlight top letter
            if i == 0:
                pygame.draw.rect(screen, "teal", text_box, border_radius=5)

            # highlight turnover notch
            if self.left[i] == self.notch:
                letter = font.render(self.notch, True, "#333333")
                pygame.draw.rect(screen, "white", text_box, border_radius=5)

            screen.blit(letter, text_box)

            # right hand side
            letter = self.right[i]
            letter = font.render(letter, True, "grey")
            text_box = letter.get_rect(center=(x+w*3/4, y+((i+1)*h)/27))
            screen.blit(letter, text_box)
