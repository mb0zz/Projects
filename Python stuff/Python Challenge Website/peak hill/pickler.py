import pickle
import urllib.request

#file = urllib.request.urlopen(http://www.pythonchallenge.com/pc/def/banner.p)


response = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")

data = pickle.load(response)

#print(data)

[0,4,0]


for i in data:
	string_to_print = ""
	for tuple in i:
		x,y = tuple
		string_to_print += x*y
	print(string_to_print)


	