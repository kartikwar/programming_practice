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

	
	def solve(self, A):
		self.pattern = A + '_' + ''.join(reversed(A))
		return len(A) - self.computeTemporaryArray()[-1], self.computeTemporaryArray()
		
		
if __name__ == "__main__":
	A = 'AACECAAAA'
	# A = []
	sol = Solution()
	out, _ = sol.solve(A=A)
	pass