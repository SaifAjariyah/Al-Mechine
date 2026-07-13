from src import app_manager

import pygame
import array

X_RES = 320
Y_RES = 240

canvas = pygame.Surface((X_RES, Y_RES))
pygame.font.init()
font = pygame.font.Font(None, 50)

def screen(state):
    canvas.fill((30, 0, 50))

    text = font.render("AL-DEVICE", True, (255,255,255))
    canvas.blit(text, (30, 20))

    for i, option in enumerate(state.option_names):
        colour = (255, 0, 155) if i == state.selected else (200, 0, 100)
        text = font.render(option, True, colour)
        canvas.blit(text, (40, 60 + i * 40))

    pixel_print(canvas)

def pixel_print(canvas):
    raw_24bit = bytearray(pygame.image.tobytes(canvas, "RGB"))
    r = raw_24bit[0::3]
    g = raw_24bit[1::3]
    b = raw_24bit[2::3]

    rgb565_data = array.array('H', (
        ((red >> 3) << 11) | ((green >> 2) << 5) | (blue >> 3)
        for red, green, blue in zip(r, g, b)
    ))

    try:
        with open("/dev/fb1", "wb") as f:
            f.write(rgb565_data.tobytes())
    except IOError:
        return False
    return True
