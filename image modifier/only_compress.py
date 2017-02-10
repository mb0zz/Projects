from PIL import Image
import os

dir = str(os.getcwd())
old_images_dir = dir + "\\uncropped"
new_images_dir = dir + "\\cropped"

for image in os.listdir(old_images_dir):

	pic_file = open(old_images_dir + "\\" + image, 'rb')
	img = Image.open(pic_file)
	img.save((new_images_dir + "\\" + image), img.format, quality=95,optimize=True)
	pic_file.close()