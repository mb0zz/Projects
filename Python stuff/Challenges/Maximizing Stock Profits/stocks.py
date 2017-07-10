'''
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

You must buy before you sell
'''
stock_prices_yesterday = [5,4,3,2,1,1]#[1, 10, 7, 5, 8, 11, 9, 21, 51]


def get_max_profit(stock_prices):

	min_val = 0
	max_val = 0
	max_profit = 0

	for i in stock_prices:
		for index in range(stock_prices.index(i), (len(stock_prices))):
			profit = (stock_prices[index] - i)
			if profit >= max_profit:
				max_profit = profit
				min_val = i
				max_val = stock_prices[index]
		
	values = min_val,max_val
	max_profit = (max_profit, values)
	return max_profit

profit,loss = get_max_profit(stock_prices_yesterday)

print("The most money you could have made was", profit[0], " (buying for", profit[1][0], " and selling for", profit[1][1])




