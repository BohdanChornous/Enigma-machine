import pygame
import string
from draw import draw
from enigma import Enigma
from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
'''
Reflector: A
Rotors: I-II-III
Plugboard: A-R, G-K, O-X
Message: A=>X
'''
# set up pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption("Enigma simulation")

# Create fons
MONO = pygame.font.SysFont("FreeMono", 25)
BOLD = pygame.font.SysFont("FreeMono", 25, bold=True)

# global variables
WIDTH = 1600
HEIGHT = 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGINS = {"top": 250, "bottom": 100, "left": 100, "right": 100}
GAP = 80

# input and output

INPUT = ""
OUTPUT = ""
PATH = []


Rotor_1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
Rotor_2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
Rotor_3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
Rotor_4 = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
Rotor_5 = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# keyboard and plugboard
KB = Keyboard()
PB = Plugboard(['AB', 'CD', 'EF'])

# define enigma machine
ENIGMA = Enigma(B, Rotor_1, Rotor_2, Rotor_3, PB, KB)

# set the rings
ENIGMA.set_rings((1, 1, 1))

# set message key
ENIGMA.set_key("CAT")

"""
# Encipher a message
message = "TESTINGTESTINGTESTINGTESTING"
for letter in message:
    print(ENIGMA.encipher(letter), end="")
"""

animating = True
while animating:

    # background color
    SCREEN.fill("#333333")

    # text input
    text = BOLD.render(INPUT, True, "white")
    text_box = text.get_rect(center=(WIDTH / 2, MARGINS["top"] / 3))
    SCREEN.blit(text, text_box)

    # text output
    text = MONO.render(OUTPUT, True, "white")
    text_box = text.get_rect(center=(WIDTH / 2, MARGINS["top"] / 3 + 25))
    SCREEN.blit(text, text_box)

    # draw enigma machine
    draw(ENIGMA, PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)

    # update screen
    pygame.display.flip()

    # track user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Rotor_3.rotate()
            elif event.key == pygame.K_SPACE:
                INPUT = INPUT + " "
                OUTPUT = OUTPUT + " "
            else:
                key = event.unicode
                if key in string.ascii_lowercase:
                    letter = key.upper()
                    INPUT = INPUT + letter
                    PATH, cipher = ENIGMA.encipher(letter)
                    OUTPUT = OUTPUT + cipher
