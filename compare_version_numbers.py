"""
Compare two version numbers version1 and version2.
f version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
"""



class Solution:
	
	def solve(self, A, B):
		A = [int(a) for a in A.split('.')]
	
		B = [int(b) for b in B.split('.')]
	
		max_length = max(len(A), len(B))
	
		A_add = max_length - len(A)
	
		B_add = max_length - len(B)
	
		A = A + [0] * A_add
	
		B = B + [0] * B_add
	
		index, result = 0, 0
	
		if A > B:
			result = 1
		if A< B:
			result = -1
	
		return result
		
if __name__ == "__main__":
	A = '01'
	B = '1'
	# A = []
	sol = Solution()
	out = sol.solve(A, B)
	pass