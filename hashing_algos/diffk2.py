'''Problem link :- https://www.interviewbit.com/problems/diffk-ii/'''

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
		status = 0
		diff_set = set([])
		
		for i in A:
			if (i - B) in diff_set:
				status = 1
				break
			elif (i+B) in diff_set:
				status = 1
				break
			else:
				diff_set.add(i)
				
		return status

if __name__ == '__main__':
	sol = Solution()
	A	= [ 77, 28, 19, 21, 67, 15, 53, 25, 82, 52, 8, 94, 50, 30, 37, 39, 9, 43, 35, 48, 82, 53, 16, 20, 13, 95, 18, 67, 77, 12, 93, 0 ]
	B = 53
	print(sol.diffPossible(A, B)) 