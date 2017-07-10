"""

Given a list_of_ints, find the highest_product you can get from three of the integers.
The input list_of_ints will always have at least three integers.


Plan:  

The highest product of three numbers in a list is always the product of the three highest numbers in the list.

Create a list of three numbers that are the three first numbers
"""
def highest_product_of_a_list(int_list):
	
	highest_three_numbers = []
	lowest_two_numbers = []
	highest_multiple = 1
	
	#Find the highest number, remove it
	#find the next highest number, remove it
	#find the final highest number, append all three to highest_three_numbers
	for number in range(3):
		num = max(int_list)
		highest_three_numbers.append(num)
		int_list.remove(num)#No need to use that number again, remove it.
		
	#Prevent errors and run faster by potentially exiting here.
	if len(int_list) < 2:
		highest_multiple = highest_three_numbers[0]*highest_three_numbers[1]*highest_three_numbers[2]
		return highest_multiple
		
	#same thing, but lowest numbers in list
	for low_num in range(2):
		num = min(int_list)
		lowest_two_numbers.append(num)
		int_list.remove(num)#no need to use that number again, remove it.

	#check if the multiple of the lowest two numbers is greater than the multiple of the 3rd and 2nd highest numbers
	#This checks if there are two negative numbers with a bigger multiple than the 2nd biggest multiple of positive numbers
	if lowest_two_numbers[0]*lowest_two_numbers[1] > highest_three_numbers[0]*highest_three_numbers[1]:
		highest_multiple = lowest_two_numbers[0]*lowest_two_numbers[1]*highest_three_numbers[2]
	else:
		for i in highest_three_numbers:
			highest_multiple *= i
			
	return highest_multiple

#testing different outcomes.
my_lists = [[-10,-9,-8,0],[0,1,2,3,4,5],[-10,6,4,1,3,-1],[-10,-10,0, 7,8,9]]

for list in my_lists:
	print(highest_product_of_a_list(list))
