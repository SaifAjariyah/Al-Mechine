from src import class_manager
from src import render
import pygame

X_RES, Y_RES = 320, 240
canvas = pygame.Surface((X_RES, Y_RES))

pygame.font.init()
font = pygame.font.Font(None, 50)

def run_app(app, state):

    canvas.fill((0, 0, 0))
    for i, option in enumerate(['calculator', '1+1 = 3.3']):
        colour = (255, 0, 0) if i == state.selected else (255, 255, 255)
        text = font.render(option, True, colour)
        canvas.blit(text, (40, 20 + i * 40))

    render.pixel_print(canvas)

EV_KEY = 1
KEY_DOWN = 1

KEY_UP_CODE = 103
KEY_DOWN_CODE = 108
KEY_ENTER_CODE = 28
KEY_Q_CODE = 16

NOTES_OPTIONS = ['calculator', '1+1 = 3.3']

def handle_input(state, ev_type, code, value):

    if ev_type != EV_KEY or value != KEY_DOWN:
        return False

    if code == KEY_DOWN_CODE:
        state.selected = (state.selected + 1) % len(NOTES_OPTIONS)
        return True

    elif code == KEY_UP_CODE:
        state.selected = (state.selected - 1) % len(NOTES_OPTIONS)
        return True

    if code == KEY_Q_CODE:
        state.mode = "Menu"
        return True

    return False

calculator_app = class_manager.AppInfo(
    "calculator",
    50,
    2,
    run_app,
    handle_input
)