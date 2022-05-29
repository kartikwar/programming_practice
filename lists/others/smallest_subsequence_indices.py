"""
Pair of indices to satisfy the Smallest subsequence.
Input:  abdc, bd    Output: 2
"""



class Solution:
	
	def solve(self, A, B):
		result = {}
		
		for char in B:
			result[char] = 0
		
		for char in A:
			if char in B:
				result[char] +=1
		
		return sum(result.values())
		
if __name__ == "__main__":
	A = 'abdcd'
	B = 'bd'
	# A = []
	sol = Solution()
	out = sol.solve(A, B)
	pass