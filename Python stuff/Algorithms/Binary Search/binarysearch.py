#binary search
import random, time
#from time import process_time
	
def binary_search(list, number):
	count = 0
	
	found = False
	bottom = 0
	top = len(list) - 1
	
	start_time = time.time()
	while not found and bottom <= top:
		count += 1
		index = (bottom + top)//2
		if list[index] == number:
			found = True
			
		elif list[index] < number:
			bottom = index + 1
			
		else:
			top = index - 1
	end_time = time.time()
	print("Found number")
	print("Binary search took a total of ", count, " tries over a time of: ", (end_time - start_time))
	return found
	
def regular_search(list, number):
	
	start_time = time.time()
	count = 0
	found = False
	for i in list:
		count += 1
		if i == number:
			found = True
			break
	end_time = time.time()
	print("regular search took a total of ", count, " tries over a time of: ", (end_time - start_time))
	return found
	

	
def run():
	b_list = []
	list_size = 100000
	highest = 100000
	lowest = 0


	for i in range(0, list_size): #create list to search
		b_list.append(i)
		
	while True:#while input isn't empty
		#assuming user is smart enough to put an integer in here
		num_to_find = int(input("Check if your number is in the list\n(Leave input blank and press enter to quit)\n>"))
		if binary_search(b_list, num_to_find) != True:
			print("Number not found by binary search")
		if regular_search(b_list, num_to_find) != True:
			print("Number not found by regular search.")
		
run()