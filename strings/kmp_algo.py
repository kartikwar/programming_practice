"""
Given an string A. The only operation allowed is to insert characters in the beginning of the string.

Find how many minimum characters are needed to be inserted to make the string a palindrome string.
"""

import math


class Solution:
	"""
	returns true if balanced, else false
	"""
	
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
	
	def KMP(self):
		self.lps = self.computeTemporaryArray()
		i, j = 0, 0
		while i < len(self.text) and j < len(self.pattern):
			if self.text[i] == self.pattern[j]:
				i = i + 1
				j = j + 1
			else:
				if j != 0:
					j = self.lps[j - 1]
				else:
					i = i + 1
		if j == len(self.pattern):
			return True
		return False
	
	def solve(self, A, pattern):
		self.pattern = pattern
		self.text = A
		result = self.KMP()
		return result


if __name__ == "__main__":
	A = 'abdeeabea'
	pattern = 'bcecba'
	fake_patterb = pattern + '_' + ''.join(reversed(pattern))
	sol = Solution()
	out = sol.solve(A=A, pattern=fake_patterb)
	a1 = [0, 0, 0, 0, 1, 0]
	pass
