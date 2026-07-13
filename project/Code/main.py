import fcntl
import pygame

from src import app_manager
from src.apps_list import notes
from src import render

from src import class_manager as classes
from src import kernal_brain

X_RES, Y_RES = 320, 240
KEY_DEVICE = "/dev/input/event0"

pygame.init()

option_ids = app_manager.list_apps(1)
option_names = app_manager.list_apps(2)
state = classes.State(option_ids, option_names, False)
queue = classes.EventQueue()

keyboard = open(KEY_DEVICE, "rb")
input_layer = classes.InputLayer(keyboard, queue)

# exclusivly grabbing the keybaord input using fcntl package 
# (to avoid accmulating input and pushing them outside program after exit)
EVIOCGRAB = 1074021776
fcntl.ioctl(keyboard, EVIOCGRAB, 1)

render.screen(state)

while state.running:

    input_layer.poll()

    changed = False 

    while not queue.empty():
        event = queue.pop()
        changed |= kernal_brain.process_event(state, event)

    if state.mode == "NOTE_EDIT":
        if changed or state.commited_text:
            notes.render_note(state)
            if state.commited_text:
                state.commited_text = False

    elif state.mode == "App":
        if changed:
            app_manager.run_app(state.current_app, state)

    else:
        if changed:
            render.screen(state)


# releasing the input
fcntl.ioctl(keyboard, EVIOCGRAB, 0)

pygame.quit()
keyboard.close()

print("Closed gracfully :)")