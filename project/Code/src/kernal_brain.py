from src import app_manager
from src.apps_list import notes

EV_KEY = 1
KEY_DOWN = 1

KEY_UP_CODE = 103
KEY_DOWN_CODE = 108
KEY_ENTER_CODE = 28
KEY_Q_CODE = 16

def process_event(state, event):

    ev_type, code, value = event

    if state.mode == "Menu":
        return handle_menu(state, ev_type, code, value)

    elif state.mode == "App":
        return handle_app(state, ev_type, code, value)
    
    elif state.mode == "NOTE_EDIT":
        return notes.handle_note_input(state, ev_type, code, value)

    return False

def handle_menu(state, ev_type, code, value):

    if ev_type != EV_KEY or value != KEY_DOWN:
        return False

    if code == KEY_DOWN_CODE:
        state.selected = (state.selected + 1) % len(state.option_ids)
        return True

    elif code == KEY_UP_CODE:
        state.selected = (state.selected - 1) % len(state.option_ids)
        return True

    elif code == KEY_ENTER_CODE:
        state.current_app = state.option_ids[state.selected]
        state.mode = "App"
        return True

    elif code == KEY_Q_CODE:
        state.running = False
        return True

    return False


def handle_app(state, ev_type, code, value):

    app = app_manager.get_app(state.current_app)

    if app and app.input:
        return app.input(state, ev_type, code, value)

    elif state.mode == "NOTE_EDIT":
        return notes.handle_note_input(state, ev_type, code, value)
    
    return False
