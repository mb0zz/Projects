import time
file = open("read.txt", "r")

string = ""
checknextind = ""
finalstring = []

letters = "abcdefghijklmnopqrstuvwxyz"

alltxt = ""

for i in file.readlines():
	for index in i.strip():
		alltxt = alltxt + index
alltxt = alltxt.strip()#removed whitespace

txtlen = len(alltxt)

index = -1

for i in alltxt:
	index += 1
	
	if index >= 3 and index <= (txtlen - 3):
		if i == i.lower():
			fir = alltxt[(index-3):index]
			lst = alltxt[index + 1:(index + 4)]

			string = fir + lst

			if string == string.upper():
				checknextind = alltxt[(index-4):index-3] + alltxt[index + 4:(index + 5)]
				
				if checknextind.lower() == checknextind:
					finalstring.append(i)
print(finalstring)

