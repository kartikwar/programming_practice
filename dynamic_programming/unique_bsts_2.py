
"""https://www.interviewbit.com/problems/unique-binary-search-trees-ii/"""

class Solution:
	# @param A : integer
	# @return an integer
	def numTrees(self, A):
		dp = [0 for i in range(A+1)]
		dp[0] = 1
		dp[1] = 1
		# dp[2] = 2

		for i in range(2, A + 1):
			sum_trees = 0
			for j in range(1, A +1):
				left_trees = dp[j-1]
				right_trees = dp[i-j]
				sum_trees += left_trees* right_trees
			dp[i] = sum_trees

		return dp[A]
 
if __name__=='__main__':
	n = 3
	sol = Solution()
	out = sol.numTrees(n)
	print(out)