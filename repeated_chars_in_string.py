import math

class Solution:
	
	def __init__(self):
		pass

	"""
	returns true if balanced, else false
	"""
	def solve(self, A):
		A= sorted(A)
		
		prev_value = None

		repeats = 1
		
		duplicates = []
		
		for i, val in enumerate(A):
			
			if val == prev_value:
				repeats += 1
			else:
				if repeats > 1:
					duplicates.append([prev_value, repeats])
					repeats = 1
			prev_value = val
		
		
		duplicates = sorted(duplicates, reverse=True, key=lambda x: x[1])
		
		return duplicates, A
		

if __name__ == "__main__":
	A = 'aaaabbbcca'
	# A = []
	sol = Solution()
	out, A = sol.solve(A=A)
	pass