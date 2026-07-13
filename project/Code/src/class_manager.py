import struct
from collections import deque

EVENT_FORMAT = "llHHI"

################################################################################
## . STATE MECHINE: 
################################################################################
class State:
    def __init__(self, option_ids, option_names, entering_app):
        self.running = True

        self.selected = 0
        self.notes_selected = 0

        self.note_text = ""
        self.current_line = ""
        self.commited_text = False
        self.note_lines = []

        self.option_ids = option_ids
        self.option_names = option_names


        self.current_app = None
        self.mode = "Menu" # there will be more modes


################################################################################
## . AppInfo: 
################################################################################
class AppInfo:
    def __init__(self, name, size, id, run_fn, input):
        self.name = name
        self.size = size
        self.id = id
        self.run = run_fn
        self.input = input


################################################################################
## . EventQueue: 
################################################################################
class EventQueue:
    def __init__(self):
        self.q = deque()

    def push(self, event):
        self.q.append(event)

    def pop(self):
        if self.q:
            return self.q.popleft()
        return None

    def empty(self):
        return len(self.q) == 0


################################################################################
## . InputLayer: 
################################################################################
class InputLayer:
    def __init__(self, keyboard, queue):
        self.keyboard = keyboard
        self.queue = queue

    def poll(self):
        raw = self.keyboard.read(struct.calcsize(EVENT_FORMAT))
        if not raw:
            return

        _, _, ev_type, code, value = struct.unpack(EVENT_FORMAT, raw)

        self.queue.push((ev_type, code, value))
