import os
import pygame
import array
import threading
from sshkeyboard import listen_keyboard, stop_listening

# Initialize ONLY the font system safely
pygame.font.init()

# Match the landscape hardware layout
X_RES = 320
Y_RES = 240

canvas = pygame.Surface((X_RES, Y_RES))
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()

options = ["Calculator", "Notes", "Option A", "Option B", "Option C"]
selected = 0
running = True

# 1. Keyboard Event Handler callback function
def on_press(key):
    global selected, running
    if key == "down":
        selected = (selected + 1) % len(options)
    elif key == "up":
        selected = (selected - 1) % len(options)
    elif key == "enter":
        print(f"\n[Action] Activated: {options[selected]}")
        # Add your menu execution hooks here!
    elif key == "q" or key == "escape":
        running = False
        stop_listening()

# 2. Spin up the background keyboard listener thread
def start_keyboard_listener():
    listen_keyboard(on_press=on_press)

input_thread = threading.Thread(target=start_keyboard_listener, daemon=True)
input_thread.start()

print("Menu interactive! Use UP/DOWN arrows to navigate, ENTER to select, 'q' to quit.")

# 3. Main Graphics Render Loop
while running:
    canvas.fill((0, 0, 0))

    for i, option in enumerate(options):
        colour = (255, 0, 0) if i == selected else (255, 255, 255)
        text = font.render(option, True, colour)
        canvas.blit(text, (40, 20 + i * 40))

    # Convert RGB888 to RGB565 bytes
    raw_24bit = pygame.image.tobytes(canvas, "RGB")
    rgb565_data = array.array('H')
    for i in range(0, len(raw_24bit), 3):
        r = raw_24bit[i] >> 3      
        g = raw_24bit[i+1] >> 2    
        b = raw_24bit[i+2] >> 3    
        pixel_16bit = (r << 11) | (g << 5) | b
        rgb565_data.append(pixel_16bit)

    try:
        with open("/dev/fb1", "wb") as f:
            f.write(rgb565_data.tobytes())
    except IOError:
        running = False

    clock.tick(30)

pygame.quit()
print("\nMenu closed gracefully.")

