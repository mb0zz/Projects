import urllib.request
import time

code = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
list = []
unique = []


#print(code)
dostuff = False
for i in code.decode("utf-8"):
	if i == "%":
		dostuff = True
	if dostuff:
		if i in unique:
			unique.remove(i)
			list.append(i)
		else:
			unique.append(i)

string = ''
			
for i in unique:
	string += i
	
print(string)
				
				
time.sleep(15)