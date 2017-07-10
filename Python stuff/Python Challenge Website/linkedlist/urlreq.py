import urllib.request
import time

def getnum(string):
	allnums = "1234567890"
	num = ""
	randvar = 0
	for i in str(string):
	
		if i in allnums:
			num = num + str(i)

	return num
			
number = 12345

while True:
	with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(number)) as response:
		html = response.read()
	print(html.strip())
	number = getnum(html)
	print(number)