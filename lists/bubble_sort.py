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
			for i in range(len(A)):
				for i in range(len(A) -1):
					if A[i] > A[i +1]:
						A = self.swap(i, i+1)
					temp = 0
		return A
if __name__ == "__main__":
	A = [5, 6, 2,3,4, 7, 8, 1]

	# A = []
	sol = Solution()
	out = sol.solve(A=A)
	pass