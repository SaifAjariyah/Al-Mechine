# import pygame
# import array
# import struct

# # Initialize ONLY the font system safely
# pygame.font.init()

# X_RES = 320
# Y_RES = 240

# canvas = pygame.Surface((X_RES, Y_RES))
# font = pygame.font.Font(None, 32)

# options = ["Calculator", "Notes", "Option A", "Option B", "Option C"]
# selected = 0

# # --- NATIVE LINUX KEYBOARD LAYER ---
# # We look for the standard system keyboard device file.
# # On a Pi, this is almost always /dev/input/event0
# KEY_DEVICE = "/dev/input/event0"

# # Linux event struct format: 2 Longs (time), 3 Shorts (type, code, value)
# EVENT_FORMAT = "llHHI"
# EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

# # EV_KEY event type is 1. Value 1 means key down (pressed)
# EV_KEY = 1
# KEY_DOWN = 1

# # Standard Linux hardware keycodes
# KEY_UP_CODE = 103
# KEY_DOWN_CODE = 108
# KEY_ENTER_CODE = 28
# KEY_Q_CODE = 16

# def render_screen():
#     canvas.fill((0, 0, 0))
#     for i, option in enumerate(options):
#         colour = (255, 0, 0) if i == selected else (255, 255, 255)
#         text = font.render(option, True, colour)
#         canvas.blit(text, (40, 20 + i * 40))

#     raw_24bit = bytearray(pygame.image.tobytes(canvas, "RGB"))
#     r = raw_24bit[0::3]
#     g = raw_24bit[1::3]
#     b = raw_24bit[2::3]

#     rgb565_data = array.array('H', (
#         ((red >> 3) << 11) | ((green >> 2) << 5) | (blue >> 3)
#         for red, green, blue in zip(r, g, b)
#     ))

#     try:
#         with open("/dev/fb1", "wb") as f:
#             f.write(rgb565_data.tobytes())
#     except IOError:
#         return False
#     return True

# # Initial Draw
# render_screen()
# print("Hardware-level keyboard parsing active. Testing immediate double-taps...")

# # Open the raw hardware input file
# try:
#     keyboard = open(KEY_DEVICE, "rb")
# except PermissionError:
#     print(f"Error: Run with sudo to read {KEY_DEVICE}")
#     exit(1)

# running = True
# while running:
#     # Read a single raw hardware event packet from the device
#     event = keyboard.read(EVENT_SIZE)
#     if not event:
#         continue
        
#     # Unpack the binary structure
#     _, _, ev_type, code, value = struct.unpack(EVENT_FORMAT, event)
    
#     # Process ONLY if it is a physical key down action
#     if ev_type == EV_KEY and value == KEY_DOWN:
#         if code == KEY_DOWN_CODE:
#             selected = (selected + 1) % len(options)
#         elif code == KEY_UP_CODE:
#             selected = (selected - 1) % len(options)
#         elif code == KEY_ENTER_CODE:
#             print(f"\n[Action] Activated: {options[selected]}")
#         elif code == KEY_Q_CODE:
#             running = False
            
#         # Push to screen instantly 
#         render_screen()

# pygame.quit()
# keyboard.close()
# print("\nMenu closed gracefully.")

