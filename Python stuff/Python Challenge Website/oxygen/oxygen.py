import urllib.request, os, sys
import PIL.Image

#From color picker and paint:
#all grey
#grey starts at 43
#ends at 51

response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png')

jpgfile = PIL.Image.open(response)

pixels = jpgfile.getdata()

width, height = jpgfile.size

print(''.join([chr(pixels.getpixel((i, height//2))[0]) for i in range(0,width,7)]))

new_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join(map(chr, new_list)))



