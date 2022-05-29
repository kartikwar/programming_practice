import math

class Solution:
	# @param A : list of integers
	# @return a list of integers

	def swap(self, i, j):
		c = A[j]
		A[j] = A[i]
		A[i] = c
		return A

	def solve(self, A):
		if A and len(A):
			# return sorted(A)
			# Traverse through 1 to len(A) 
			for i in range(1, len(A)): 

				key = A[i] 

				# Move elements of A[0..i-1], that are 
				# greater than key, to one position ahead 
				# of their current position 
				j = i-1
				
				while j >= 0 and key < A[j] : 
						A[j + 1] = A[j] 
						j -= 1
				
				A[j + 1] = key 
						

		return A

if __name__ == "__main__":
	A = [5, 6, 2,3,4, 7, 8, 1]

	# A = []
	sol = Solution()
	out = sol.solve(A=A)
	pass