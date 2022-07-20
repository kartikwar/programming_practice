'''
Say you have an array, A, for which the ith element is 
the price of a given stock on day i.

Design an algorithm to find the maximum profit.

You may complete as many transactions as you like (i.e., buy 
one and sell one share of the stock multiple times).

However, you may not engage in multiple transactions at the 
same time (ie, you must sell the stock before you buy again).

Constraints:

0 <= len(A) <= 1e5
1 <= A[i] <= 1e7

Example:

Input 1:
    A = [1, 2, 3]


Output 1:
    2

Explanation 1:
    => Buy a stock on day 0.
    => Sell the stock on day 1. (Profit +1)
    => Buy a stock on day 1.
    => Sell the stock on day 2. (Profit +1)



Overall profit = 2


Input 2:
    A = [5, 2, 10]

Output 2:
    8

Explanation 2:
    => Buy a stock on day 1.
    => Sell the stock on on day 2. (Profit +8)

Overall profit = 8
'''




class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):
		if len(A) < 1:
			return 0
		dp = [-1 for i in range(len(A))]
		dp[0] = A[0]
		min_profit = A[0]

		for i in range(1,len(A)):
			if A[i] == min_profit:
				dp[i] = min_profit

			if A[i] > min_profit:
				dp[i] = min_profit
				min_profit = A[i]
			
			elif A[i] < min_profit:
				min_profit = A[i]
				dp[i] = min_profit
		
		profits = sum([A[i] - dp[i] for i in range(len(A))])
		return profits



if __name__ == '__main__':
	sol = Solution()
	A = []
	print(sol.maxProfit(A))