'''def member(dictionary, list):
	if len(list) < 1:
		return("List too short!  Try again")
	match = 0
	for key in mydict:
		if key == key in list:
			print(key, " is in my list")
			match = match + 1
		else:
			print(key, " is not in my list.")
	return(str(match))'''
def word_count(dict, list):
	if len(list) < 1:
		print("List too short, try again.")
		return(False)
	match = 0
	for key in list:
		if (key.lower()) == key in dict:
			match += 1
			print(key," is in my list ", str(match), " times")
		else:
			print("Key not in my list")
	return(match)

mydict = {"names":{"first":"matt", "last": "bozzay"}, "job":"stuff"}
mylist = []
del mydict["names"]
mydict.update({"job" : "ninja"})
while True:
	print(mydict)
	lappend = input("Add an item to your list, hit enter to leave")
	if len(lappend) < 1:
		word_count(mydict, mylist)
		break
	
	else:
		mylist.append(lappend)
		print(mylist)