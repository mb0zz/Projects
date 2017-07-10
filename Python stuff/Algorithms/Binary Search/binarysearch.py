#binary search
import random, time
#from time import process_time
	
def binary_search(list, number):
	count = 0
	
	found = False
	bottom = 0
	top = len(list) - 1
	
	timer = time.process_time()
	
	while not found and bottom <= top:
		count += 1
		index = (bottom + top)//2
		
		if list[index] == number:
			found = True
			return True
			
		elif list[index] < number:
			bottom = index + 1
			
		else:
			top = index - 1
	print("Binary search took a total of ", count, " tries over a time of: ", (timer))
	return False
	
def regular_search(list, number):
	
	timer1 = time.process_time()
	count = 0
	for i in list:
		count += 1
		if i == number:
			break
	
	print("regular search took a total of ", count, " tries over a time of: ", timer1)
	return True
	

	
def run():
	b_list = []
	list_size = 1000
	highest = 2000
	lowest = 0


	for i in range(0, list_size): #create list to search
		b_list.append(random.randint(lowest, highest))
		
	while True:#while input isn't empty
		#assuming user is smart enough to put an integer in here
		num_to_find = int(input("Check if your number is in the list\n(Leave input blank and press enter to quit)\n>"))
		if binary_search(b_list, num_to_find) != True:
			print("Number not found by binary search")
		if regular_search(b_list, num_to_find) != True:
			print("Number not found by regular search.")
		
run()