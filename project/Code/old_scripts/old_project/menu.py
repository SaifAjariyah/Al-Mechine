import pygame
import time

pygame.init()

W, H = 240, 320

screen = pygame.Surface((W, H))
font = pygame.font.Font(None, 40)

FB = open("/dev/fb1", "wb")

options = ["Calculator", "Notes", "A", "B"]
selected = 0

def draw():
    screen.fill((0, 0, 0))

    for i, opt in enumerate(options):
        color = (255, 0, 0) if i == selected else (255, 255, 255)
        text = font.render(opt, True, color)
        screen.blit(text, (20, 20 + i * 50))

    FB.seek(0)
    FB.write(pygame.image.tostring(screen, "RGB"))

while True:
    draw()
    time.sleep(0.03)
