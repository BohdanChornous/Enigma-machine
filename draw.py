import pygame


def draw(enigma, path, screen, width, height, margins, gap, font):

    # width and height of components
    w = (width - margins["left"] - margins["right"] - 5 * gap) / 6
    h = height - margins["top"] - margins["bottom"]

    # path coordinates
    y_coordinates = [margins["top"]+((signal+1)*h/27) for signal in path]
    x_coordinates = [width-margins["right"] - w/2]  # keyboard
    for i in [4, 3, 2, 1, 0]:  # forward path
        x_coordinates.append(margins["right"] + i * (w + gap) + w * 3 / 4)
        x_coordinates.append(margins["right"] + i * (w + gap) + w * 1 / 4)
    x_coordinates.append(margins["left"] + w * 3 / 4)  # reflector
    for i in [1, 2, 3, 4]:  # backward path
        x_coordinates.append(margins["right"] + i * (w + gap) + w * 1 / 4)
        x_coordinates.append(margins["right"] + i * (w + gap) + w * 3 / 4)
    x_coordinates.append(width - margins["right"] - w / 2)

    # draw the path
    if len(path) > 0:
        for i in range(1, 21):
            if i < 10:
                color = "#43aa8b"
            elif i < 12:
                color = "#f9c74f"
            else:
                color = "#e63946"
            start = (x_coordinates[i-1], y_coordinates[i-1])
            end = (x_coordinates[i], y_coordinates[i])
            pygame.draw.line(screen, color, start, end, width=5)

    # base coordinates
    x = margins["left"]
    y = margins["top"]

    # draw enigma components
    for component in [enigma.reflector, enigma.rotor_1, enigma.rotor_2,
                      enigma.rotor_3, enigma.plugboard, enigma.keyboard]:
        # draw enigma machine
        component.draw(screen, x, y, w, h, font)
        x += w + gap

    # add names
    names = ["Reflector", "Left Rotor", "Middle Rotor", "Right Rotor", "Plugboard", "Keyboard"]
    y = margins["top"] * 0.8
    for i in range(len(names)):
        x = margins["left"] + w/2 + i * (w + gap)
        title = font.render(names[i], True, "white")
        text_box = title.get_rect(center=(x, y))
        screen.blit(title, text_box)
