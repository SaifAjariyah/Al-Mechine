import os
import pygame
import array

# Initialize ONLY the font system safely
pygame.font.init()

# SWAPPED: Forcing landscape dimensions to match the driver's native stride
X_RES = 320
Y_RES = 240

# Create a standard canvas to render text onto
canvas = pygame.Surface((X_RES, Y_RES))

font = pygame.font.Font(None, 32) # Slightly smaller font to fit the 240 height cleanly
clock = pygame.time.Clock()

options = ["Calculator", "Notes", "Option A", "Option B", "Option C"]
selected = 0

print("Menu script started. Testing landscape stride on /dev/fb1...")

running = True
while running:
    # 1. Draw the UI on our 24-bit surface
    canvas.fill((0, 0, 0))

    for i, option in enumerate(options):
        colour = (255, 0, 0) if i == selected else (255, 255, 255)
        text = font.render(option, True, colour)
        
        # Adjusted padding: Center it a bit more on the 320-pixel wide layout
        canvas.blit(text, (40, 20 + i * 40))

    # 2. Get the raw 24-bit RGB buffer from Pygame
    raw_24bit = pygame.image.tobytes(canvas, "RGB")

    # 3. Convert RGB888 to RGB565 bytes
    rgb565_data = array.array('H')
    for i in range(0, len(raw_24bit), 3):
        r = raw_24bit[i] >> 3      
        g = raw_24bit[i+1] >> 2    
        b = raw_24bit[i+2] >> 3    
        
        pixel_16bit = (r << 11) | (g << 5) | b
        rgb565_data.append(pixel_16bit)

    # 4. Blast the data to the display
    try:
        with open("/dev/fb1", "wb") as f:
            f.write(rgb565_data.tobytes())
    except IOError as e:
        print(f"OS Error writing to /dev/fb1: {e}")
        running = False

    clock.tick(30)

pygame.quit()

