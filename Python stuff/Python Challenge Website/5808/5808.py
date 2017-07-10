from PIL import Image

im = Image.open("cave.jpg")
size = im.size

drawer = Image.new("RGB", (int(size[0]/2), int(size[1]/2)), "white")

img = im.load()

countx = 1
county = 1
pixels = []

for x in range(size[0]):
	if countx == 1:
		countx -= 1
		for y in range(size[1]):
			if county == 1:
				pixels.append((x,y))
				county = 0
			else:
				county += 1
	elif countx == 0:
		countx += 1
		
pixel_colors = []

for i in pixels:
	pixel_colors.append(img[i])

counter = 0
for pixel in pixels:
	pix = (int(pixel[0]/2),int(pixel[1]/2))
	drawer.putpixel(pix, pixel_colors[counter])
	counter += 1
	
drawer.show()