'''
Given a 2D integer array A of size M x N, you need to find 
a path from top left to bottom right which minimizes the 
sum of all numbers along its path.

NOTE: You can only move either down or right at any point in time. 



Input Format
First and only argument is an 2D integer array A of size M x N.



Output Format
Return a single integer denoting the minimum sum of a path 
from cell (1, 1) to cell (M, N).



Example Input
Input 1:

A = [[1, 3, 2]
    [4, 3, 1]
    [5, 6, 1]]


Example Output
Output 1: 8


Example Explanation
Explanation 1:

 The path is 1 -> 3 -> 2 -> 1 -> 1
 So ( 1 + 3 + 2 + 1 + 1) = 8

'''

import sys
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def minPathSum(self, A):
		x_length = len(A)
		y_length = len(A[0])
		dp = [[0 for i in range(y_length)] for j in range(x_length)]
		dp[0][0] = A[0][0]
		for i in range(x_length):
			for j in range(y_length):
				left_val, top_val = sys.maxsize, sys.maxsize
				if j > 0:
					left_val = dp[i][j-1]
				if i > 0:
					top_val = dp[i-1][j]

				min_val = min(left_val, top_val)
				if min_val != sys.maxsize:
					dp[i][j] = min_val + A[i][j]
		return dp[x_length -1][y_length -1]


if __name__ == '__main__':
	sol = Solution()
	A = [[1, 3, 2],
        [4, 3, 1],
        [5, 6, 1]]
	out = sol.minPathSum(A)
	print(out)