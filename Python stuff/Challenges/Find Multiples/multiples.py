'''
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7*3*4, 1*3*4, 1*7*4, 1*7*3]

Do not use division in your solution.
'''


def get_products_of_all_ints_except_at_index(list):
	
	list_of_multiples = []
	popped_list = list
	
	counter = 0
	
	for i in list:
	
		popped_list.remove(i)
		
		multiple = 1
		for index in popped_list:
			multiple *= index
			
		list_of_multiples.append(multiple)
		popped_list.insert(counter, i)
		counter += 1
		
	return(list_of_multiples)

my_list = [9,2,6,3]
x = get_products_of_all_ints_except_at_index(my_list)
print(x)








