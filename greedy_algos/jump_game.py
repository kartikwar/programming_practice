'''https://www.interviewbit.com/problems/jump-game-array/'''
class Solution:
	# @param A : list of integers
	# @return an integer
	def canJump(self, A):
		status = 1
		reachable = 0
		for i in range(len(A)):
			if reachable < i:
				status = 0
				return status
			reachable = max(reachable, i + A[i])
		return status 


if __name__ == '__main__':
	sol = Solution()
	A = [3,2,1,0,4]
	print(sol.canJump(A))