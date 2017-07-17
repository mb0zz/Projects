import random
#Create a list with 100 items between 1 and 1000
mylist = []
for index in range(100):
	mylist.append(random.randint(0,1000))

#Use greedy algorithm to find the largest number in an unordered list

#start with the first num in the list, then check all nums against it.
highest_num = mylist[0]

print(mylist)#print list to check
#a common error is to start with 0, however, this will not work if the list is full of numbers smaller than 0
for i in range(len(mylist)):
	num_to_check = mylist[i]
	if highest_num < num_to_check:
		print("Highest number was %d new highest number is %d" % (highest_num, num_to_check))#just to have some output.
		highest_num = num_to_check
