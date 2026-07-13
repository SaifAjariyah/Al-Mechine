from PIL import Image, ImageDraw
import time

fb = open("/dev/fb0", "wb")

W, H = 240, 320

while True:
	img = Image.new("RGB", (W, H), "black")
	draw = ImageDraw.Draw(img)

	draw.text((20,20), "SPI WORKING!", fill="white")
	draw.text((20,20), "TEST SCREEN", fill="red")

	fb.seek(0)
	fb.write(img.tobytes())

	time.sleep(0.5)
