"""
Given an string A. The only operation allowed is to insert characters in the beginning of the string.

Find how many minimum characters are needed to be inserted to make the string a palindrome string.
"""

import math

class Solution:

	'''
	method used to compute lps in kmp algo
	'''
	def computeTemporaryArray(self):
		lps = [0] * len(self.pattern)
		index = 0
		i = 1
		while i < len(self.pattern):
			if self.pattern[i] == self.pattern[index]:
				lps[i] = index + 1
				index = index + 1
				i = i + 1
			else:
				if index != 0:
					index = lps[index - 1]
				else:
					lps[i] = 0
					i = i + 1
		return lps
	
	def solve_(self, A):
		if len(A) <= 1:
			return 0
		
		start, end, palin_at = 0, len(A) - 1, len(A) - 1
		
		while start < end:
			if A[start] == A[end]:
				start += 1
				end -= 1
			else:
				end = palin_at - 1
				palin_at = end
				start = 0
		
		return len(A) - 1 - palin_at
	

	def solve(self, A):
		if len(A) <= 1:
			return 0
		
		palin_at = len(A) - 1
		start = 0
		end = len(A) - 1
	
		while start <= end:
			if A[start] == A[end]:
				start = start + 1
				end = end - 1
			else:
				end = palin_at - 1
				palin_at = end
				start = 0
		
		return len(A) - (1 + palin_at)
		
if __name__ == "__main__":
	A = 'babb'
	# A = []
	sol = Solution()
	out = sol.solve_(A=A)
	pass