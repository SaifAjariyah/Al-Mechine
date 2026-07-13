import os
import pygame

os.environ["SDL_FBDEV"] =  "/dev/fb1"
pygame.init()

screen = pygame.display.set_mode((240, 320))
font = pygame.font.Font(None, 60)
clock = pygame.time.Clock()

options = ["Calculator", "Notes", "a", "b", "c", "d", "e"]
selected = 0

running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				selected += 1
				if selected >= len(options):
					selected = 0
			elif event.key == pygame.K_UP:
				selected -= 1
				if selected < 0:
					selected = len(options) - 1

	screen.fill((0,0,0))

	for i, option in enumerate(options):
		if i == selected:
			colour = (255,0,0)
		else:
			colour = (255,255,255)

		text = font.render(option, True, colour)
		screen.blit(text, (200, 150 + i * 60))

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
