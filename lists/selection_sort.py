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
			for i, x in enumerate(A[:-1]):
				min_x = A[i]
				min_i = i

				for j in range(i + 1, len(A)):
					if A[j] < min_x:
						min_x = A[j]
						min_i = j
				
				A = self.swap(i, min_i)
				temp = 0
		return A
if __name__ == "__main__":
	A = [2,3,4, 1]

	# A = []
	sol = Solution()
	out = sol.solve(A=A)
	pass