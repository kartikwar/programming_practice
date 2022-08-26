'''
Problem Link: https://www.interviewbit.com/courses/programming/dynamic-programming
'''

class Solution:
	# @param A : list of list of integers
	# @return an integer
	def solve(self, A):
		dp = [1 for i in range(len(A))]
		
		for i in range(1, len(A)):
			max_count = 0
			for j in range(0, i):
				if A[i][0] > A[j][1]:
					curr_count = dp[j] + 1
					if curr_count > max_count:
						max_count = curr_count
						dp[i] = curr_count
						
		return max(dp)

if __name__ == '__main__':
	sol = Solution()
	# A = [[5, 24], [39, 60], [15, 28], [27, 40],[50, 90]]
	A = [[98, 894],[397, 942], [70, 519], [258, 456], [286, 449],[516, 626],
  		[370, 873],[214, 224],[74, 629],[265, 886],[708, 815],[394, 770],[56, 252]]
	print(sol.solve(A))