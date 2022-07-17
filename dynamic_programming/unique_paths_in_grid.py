'''
Given a grid of size m * n, lets assume you are starting at (1,1) and 
your goal is to reach (m,n). At any instance, if you are on (x,y), 
you can either go to (x, y + 1) or (x + 1, y).

Now consider if some obstacles are added to the grids. How many unique 
paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Example :

There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''


class Solution:
	# @param A : list of list of integers
	# @return an integer

	def nor(self, ele1, ele2):
		return not(ele1 or ele2)

	def uniquePathsWithObstacles(self, A):
		rows, cols = len(A), len(A[0])
		dp = [[0 for i in range(cols)] for j in range(rows)]

		if A[0][0] == 0:
			dp[0][0] =1

		for row in range(rows):
			for col in range(cols):
				if A[row][col] == 1:
					continue
				else:
					update_row, update_col = 0, 0
					curr_ele = A[row][col]
				
					if row < rows -1:
						next_ele = A[row+1][col]
						update_row = self.nor(curr_ele, next_ele)
					if col < cols -1:
						next_ele = A[row][col +1]
						update_col = self.nor(curr_ele, next_ele)
					if update_row:
						dp[row+1][col] += dp[row][col]
					if update_col:
						dp[row][col+1] += dp[row][col]

		return dp[rows-1][cols-1]




if __name__ == '__main__':
	sol = Solution()
	A = [[0,0,0], [0,0,0], [0,0,0]]
	print(sol.uniquePathsWithObstacles(A))