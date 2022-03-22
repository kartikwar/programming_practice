import math

class Solution:
	
	def __init__(self):
		pass

	"""
	returns true if balanced, else false
	"""
	def solve(self, A):
		A= sorted(A)
		
		non_duplicates = []
		
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
			
		for i, val in enumerate(A):
			
			if i == 0:
				non_duplicates.append(A[i])
			
			else:
				if A[i] == A[i-1]:
					print('found dupli')
				else:
					non_duplicates.append(A[i])
				
		return duplicates, non_duplicates
		

if __name__ == "__main__":
	A = [1, 3 , 4, 7, 1, 5, 6, 3, 2, 3 , 6, 6, 7, 8]
	# A = []
	sol = Solution()
	out, A = sol.solve(A=A)
	pass