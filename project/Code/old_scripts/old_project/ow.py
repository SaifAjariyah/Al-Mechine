import os
import pygame
import array
import threading
from sshkeyboard import listen_keyboard, stop_listening

# Initialize ONLY the font system safely
pygame.font.init()

# Hardware layout dimensions
X_RES = 320
Y_RES = 240

canvas = pygame.Surface((X_RES, Y_RES))
font = pygame.font.Font(None, 32)
clock = pygame.time.Clock()

options = ["Calculator", "Notes", "Option A", "Option B", "Option C"]
selected = 0
running = True

# 1. Keyboard Event Handler
def on_press(key):
    global selected, running
    if key == "down":
        selected = (selected + 1) % len(options)
    elif key == "up":
        selected = (selected - 1) % len(options)
    elif key == "enter":
        print(f"\n[Action] Activated: {options[selected]}")
    elif key == "q" or key == "escape":
        running = False
        stop_listening()

# Spin up the background input listener
input_thread = threading.Thread(target=lambda: listen_keyboard(on_press=on_press), daemon=True)
input_thread.start()

print("Zero-dependency high-performance menu active...")

while running:
    # Render the UI
    canvas.fill((0, 0, 0))

    for i, option in enumerate(options):
        colour = (255, 0, 0) if i == selected else (255, 255, 255)
        text = font.render(option, True, colour)
        canvas.blit(text, (40, 20 + i * 40))

    # 2. ULTRA-FAST NATIVE BIT CONVERSION
    # Extract the raw 24-bit bytes from Pygame
    raw_24bit = bytearray(pygame.image.tobytes(canvas, "RGB"))

    # Isolate color channels instantly using Python's native fast-slicing engine
    r = raw_24bit[0::3]  # Every 3rd byte starting at 0 (Red)
    g = raw_24bit[1::3]  # Every 3rd byte starting at 1 (Green)
    b = raw_24bit[2::3]  # Every 3rd byte starting at 2 (Blue)

    # Re-pack the isolated streams into a fast 16-bit integer array
    rgb565_data = array.array('H')
    
    # This zipped loop runs incredibly fast because the heavy data slicing happened above
    for red, green, blue in zip(r, g, b):
        pixel_16bit = ((red >> 3) << 11) | ((green >> 2) << 5) | (blue >> 3)
        rgb565_data.append(pixel_16bit)

    # 3. Write directly to the display
    try:
        with open("/dev/fb1", "wb") as f:
            f.write(rgb565_data.tobytes())
    except IOError:
        running = False

    clock.tick(30)

pygame.quit()
print("\nMenu closed gracefully.")

