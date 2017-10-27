from PIL import Image
from resizeimage import resizeimage
import os

dir = str(os.getcwd())
old_images_dir = dir + "\\uncropped"
new_images_dir = dir + "\\cropped"

################Change these#####################
intended_width = 200
picture_quality = 80
#################################################

for image in os.listdir(old_images_dir):

	pic_file = open(old_images_dir + "\\" + image, 'rb')
	img = Image.open(pic_file)
	print("Dimensions before: ",img.size)
	if img.size[0] < intended_width:
		img = resizeimage.resize_width(img, img.size[0])
	else:
		img = resizeimage.resize_width(img, intended_width)
	img.save((new_images_dir + "\\" + image), img.format, quality=picture_quality,optimize=True)
	print("Dimensions after: ",img.size)
	pic_file.close()