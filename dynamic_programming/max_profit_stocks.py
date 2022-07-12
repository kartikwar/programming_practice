'''
Problem Description

Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Return the maximum possible profit.



Problem Constraints
0 <= len(A) <= 7e5

1 <= A[i] <= 1e7



Input Format
The first and the only argument is an array of integers, A.



Output Format
Return an integer, representing the maximum possible profit.



Example Input
Input 1:

 A = [1, 2]
Input 2:

 A = [1, 4, 5, 2, 4]


Example Output
Output 1:
 1
Output 2:

 4
'''


import sys
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):
		max_profit = 0
		dp = len(A) * [sys.maxsize]
		min_profit = sys.maxsize
		for i in range(len(A)):
			min_profit = min(A[i], min_profit)
			dp[i] = min_profit

		
		if len(A):
			max_profit = max([A[i] - dp[i] for i in range(len(A))])
		
		return max_profit

if __name__ == '__main__':
	sol = Solution()
	print(sol.maxProfit([1,4,5,2,4]))