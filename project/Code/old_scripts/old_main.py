# import pygame 
# import struct

# from src import app_manager as apps
# from src import render
# from src import input_manager as input
# from collections import deque

# pygame.font.init()

# ########################
# ## 1. SYSTEM INFO: #####
# ########################
# X_RES = 320
# Y_RES = 240

# KEY_DEVICE = "/dev/input/event0"
# EVENT_FORMAT = "llHHI"
# EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

# canvas = pygame.Surface((X_RES, Y_RES))
# font = pygame.font.Font(None, 32)
# ########################


# ########################
# ## 2. STATE MECHINE: ###
# ########################
# options = apps.get_apps()

# class State:
#     def __init__(self, options):
#         self.running = True

#         self.selected = 0
#         self.options = options

#         self.current_app = None
#         self.mode = "menu" # there will be more modes

# state = State(options)
# ########################

# render.screen(state, canvas, font)

# try:
#     keyboard = open(KEY_DEVICE, "rb")
# except PermissionError:
#     print(f"Error: Run with sudo to read {KEY_DEVICE}")
#     exit(1)

# state.running = True
# while state.running:

#     event = keyboard.read(EVENT_SIZE)

#     if not event:
#         continue

#     input.process(state, canvas, font, event)
    

# pygame.quit()
# input.close_keyboard(keyboard)
# print("\nMenu closed gracefully.")
