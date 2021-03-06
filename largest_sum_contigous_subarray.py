import math
import sys

class Solution:

	def local_maximum(self, i, A):
		if i == len(A) -1 :
			return A[i]
		else:
			return max(A[i], A[i] + self.local_maximum(i-1, A)) 

	"""
	returns smallest sum
	"""
	def solve(self, A):
		n = len(A)
		local_max = 0
		global_max = -sys.maxsize

		for i in range(n):
			local_max = max(A[i], A[i] + local_max)
			if local_max > global_max:
				global_max = local_max
		return global_max




if __name__ == "__main__":
	A = [3, 4, 2, -3, -1, 7, -5]
	# A = []
	sol = Solution()
	out = sol.solve(A=A)
	pass