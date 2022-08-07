'''
Given an array A of sorted integers and another 
non negative integer k, find if there exists 2 
indices i and j such that A[i] - A[j] = k, i != j.

Problem link https://www.interviewbit.com/problems/diffk/
'''

class Solution:
	
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
		start = 0
		end = 1

		# A = sorted(A)

		if len(A) > 1:
			while end < len(A) and start < len(A):
				diff = A[end] - A[start]
				if  diff == B:
					if start != end:
						return 1
					else:
						end = end + 1
				elif diff < B:
					end = end + 1
				else:
					start = start + 1  
		
		return 0

if __name__ == '__main__':
	A = [ -509, -5 ]
	B = -95173

	sol = Solution()
	print(sol.diffPossible(A, B))