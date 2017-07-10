'''
'''


#returns the number of ways to split the denominations
def find_highest_denomination(list_of_coins, value):
	
	if value <= 0:
		return 0
		
	solutions = True
	
	count = 0
	index = -1
	
	while solutions:

		while value > 0:
			print(index)
			
			if value - list_of_coins[index] > 0:
				value -= list_of_coins[index]
			
			elif value - list_of_coins[index] < 0:
				index -= 1
				
		if index == -1:
			solutions == False
			
		count += 1
		
	return count
	
print(find_highest_denomination([1,2,3], 4))