# import struct
# from src import render

# # Linux event struct format: 2 Longs (time), 3 Shorts (type, code, value)
# EVENT_FORMAT = "llHHI"

# EV_KEY = 1
# KEY_DOWN = 1

# # Standard Linux hardware keycodes
# KEY_UP_CODE = 103
# KEY_DOWN_CODE = 108
# KEY_ENTER_CODE = 28
# KEY_Q_CODE = 16

# # Process ONLY if it is a physical key down action
# def process(state, canvas, font, event):
#     # Read a single raw hardware event packet from the device

#     # Unpack the binary structure
#     _, _, ev_type, code, value = struct.unpack(EVENT_FORMAT, event)
    
#     # Process ONLY if it is a physical key down action
#     if ev_type == EV_KEY and value == KEY_DOWN:
#         if code == KEY_DOWN_CODE:
#             state.selected = (state.selected + 1) % len(state.options)
#         elif code == KEY_UP_CODE:
#             state.selected = (state.selected - 1) % len(state.options)
#         elif code == KEY_ENTER_CODE:
#             print(f"\n[Action] Activated: {state.options[state.selected]}")
#         elif code == KEY_Q_CODE:
#             state.running = False
            
#         # Push to screen instantly 
#         render.screen(state, canvas, font)

#     return state

# def close_keyboard(keyboard):
#     keyboard.close()
