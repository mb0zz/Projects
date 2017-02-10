from PIL import Image
from resizeimage import resizeimage
import os

dir = str(os.getcwd())
old_images_dir = dir + "\\uncropped"
new_images_dir = dir + "\\cropped"

################Change these#####################
intended_width = 800
picture_quality = 95
#################################################

for image in os.listdir(old_images_dir):

	pic_file = open(old_images_dir + "\\" + image, 'rb')
	img = Image.open(pic_file)
	print("Dimensions before: ",img.size)
	if img.size[0] < intended_size:
		img = resizeimage.resize_width(img, img.size[0])
	else:
		img = resizeimage.resize_width(img, intended_size)
	img.save((new_images_dir + "\\" + image), img.format, quality=picture_quality,optimize=True)
	print("Dimensions after: ",img.size)
	pic_file.close()