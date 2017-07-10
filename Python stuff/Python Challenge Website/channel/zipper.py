import zipfile, time

def getnum(string):
	allnums = "1234567890"
	num = ""
	randvar = 0
	for i in str(string):
		if i in allnums:
			num = num + str(i)
	return num
number = "90052"
filelist = []

while True:
	filelist.append(number + ".txt")
	string_do = ""
	try:
		file = open(("files//" + number + ".txt"), "r")
	except:
		break
	
	for line in file.readlines():
		for i in line.strip():
			string_do += i
	
	number = getnum(string_do)
	if len(number) < 1:
		break
	file.close()

zfile = zipfile.ZipFile('channel.zip', 'r')
string = ""
for filename in filelist:
	info = zfile.getinfo(filename)
	if ord(info.comment) - 10 == 0:
		print(string.strip())
		string = ""
	else:
		string += (str(info.comment)[1:]).replace("'", "")