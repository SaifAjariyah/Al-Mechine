from src import render
from src import class_manager
import pygame
import json



X_RES, Y_RES = 320, 240
canvas = pygame.Surface((X_RES, Y_RES))

pygame.font.init()
font = pygame.font.Font(None, 50)

options = ['Make new Note', 'Load old Notes']

def run_app(app, state):
    canvas.fill((255, 255, 255))
    for i, option in enumerate(options):
        colour = (255, 0, 155) if i == state.notes_selected else (255, 0, 255)
        text = font.render(option, True, colour)
        canvas.blit(text, (40, 120 + i * 40))

    render.pixel_print(canvas)


EV_KEY = 1
KEY_DOWN = 1

KEY_ESC = 1
KEY_UP_CODE = 103
KEY_DOWN_CODE = 108
KEY_ENTER_CODE = 28
KEY_Q_CODE = 16

KEY_LEFT_SHIFT = 42
KEY_RIGHT_SHIFT = 54

KEY_MAP = {
    2: "1", 3: "2", 4: "3", 5: "4", 6: "5",
    7: "6", 8: "7", 9: "8", 10: "9", 11: "0",

    16: "q", 17: "w", 18: "e", 19: "r", 20: "t",
    21: "y", 22: "u", 23: "i", 24: "o", 25: "p",

    30: "a", 31: "s", 32: "d", 33: "f", 34: "g",
    35: "h", 36: "j", 37: "k", 38: "l", 39: ";",

    44: "z", 45: "x", 46: "c", 47: "v", 48: "b",
    49: "n", 50: "m", 51: ",", 52: ".", 53: "/",
}

SHIFT_MAP = {
    2: "!",
    3: "@",
    4: "#",
    5: "$",
    6: "%",
    7: "^",
    8: "&",
    9: "*",
    10: "(",
    11: ")",

    12: "_",   # minus key usually
    13: "+",   # equals key usually

    26: "[",
    27: "]",
    40: "'",
    41: "`",
    43: "\\",
}

def handle_input(state, ev_type, code, value):

    if ev_type != EV_KEY or value != KEY_DOWN:
        return False

    if code == KEY_DOWN_CODE:
        state.notes_selected = (state.notes_selected + 1) % len(options)
        return True

    elif code == KEY_UP_CODE:
        state.notes_selected = (state.notes_selected - 1) % len(options)
        return True

    elif code == KEY_ENTER_CODE:
        if state.notes_selected == 0:
            print("new note!")
            state.mode = "NOTE_EDIT"
            print("MODE NOW:", state.mode)
            state.note_text = ""
            return True

        elif state.notes_selected == 1:
            print("loading note!")

            with open("mydata.json") as f:
                data = json.load(f)

            state.note_lines = data["notes_app"]
            state.current_line = ""
            state.mode = "NOTE_EDIT"
            return True


    if code == KEY_Q_CODE:
        state.mode = "Menu"
        return True

    return False


def render_note(state):
    canvas.fill((255, 246, 215))
    
    all_lines = state.note_lines + [state.current_line]

    for i, line in enumerate(all_lines):
        fontText = pygame.font.Font(None, 20)
        text = fontText.render(line, True, (79, 60, 0))
        canvas.blit(text, (10, 20 + i * 40))

    for i in range(6):
        #                        (surface, color, start_pos, end_pos, width)
        pygame.draw.line(canvas, (79, 60, 0), (0, 40 + i * 40), (320, 40 + i * 40), 1)

    render.pixel_print(canvas)


KEY_UP = 0
KEY_DOWN = 1
def handle_note_input(state, ev_type, code, value):

    if ev_type != EV_KEY:
        return False

    # ---------------- SHIFT (MUST RUN BEFORE FILTER) ----------------
    if code in (KEY_LEFT_SHIFT, KEY_RIGHT_SHIFT):
        if value == KEY_DOWN:
            state.shift = True
        elif value == KEY_UP:
            state.shift = False
        return True

    # ---------------- IGNORE ONLY NON-PRESS KEYS ----------------
    if value != KEY_DOWN:
        return False

    shift = getattr(state, "shift", False)

    # ---------------- TEXT INPUT ----------------

    if code == 28:  # Enter
        state.note_lines.append(state.current_line)
        state.current_line = ""
        return True

    if code == 57:  # Space
        state.current_line += " "
        return True

    if code == 14:  # Backspace
        state.current_line = state.current_line[:-1]
        return True

    if code == KEY_ESC:
        state.note_lines.append(state.current_line)
        state.current_line = ""

        with open('mydata.json', 'w') as f:
            json.dump({"notes_app": state.note_lines}, f, indent=4)

        state.mode = "Menu"
        return True

    # ---------------- CHARACTER MAP ----------------

    if shift and code in SHIFT_MAP:
        state.current_line += SHIFT_MAP[code]
        return True

    if code in KEY_MAP:
        state.current_line += KEY_MAP[code]
        return True

    return False

notes_app = class_manager.AppInfo(
    "Notes",
    50,
    1,
    run_app,
    handle_input
)
