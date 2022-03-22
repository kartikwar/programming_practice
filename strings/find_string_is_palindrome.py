import math

class Solution:
	
	def __init__(self):
		pass

	"""
	returns true if balanced, else false
	"""
	def solve(self, A):
		status = True
		start = 0
		end = len(A) -1
		
		while start <= end:
			if A[start] != A[end]:
				status = False
				break
			
			start  = start + 1
			end = end - 1
		
		return status

if __name__ == "__main__":
	A = 'c'
	# A = []
	sol = Solution()
	out = sol.solve(A=A)
	pass