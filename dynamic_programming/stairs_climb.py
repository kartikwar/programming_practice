'''Problem link :- https://www.interviewbit.com/problems/stairs/'''

class Solution:
	# @param A : integer
	# @return an integer
	def climbStairs(self, A):
		if A < 1:
			return A

		dp = [0 for i in range(A + 1)]
		dp[0] = 1
		dp[1] = 1

		for i in range(2, len(dp)):
			dp[i] = dp[i-1] + dp[i-2]
		
		return dp[-1]
		

if __name__ == '__main__':
	sol = Solution()
	sol.climbStairs(A=0)