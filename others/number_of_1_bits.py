"""
Write a function that takes an unsigned integer and returns the number of 1 bits it has.
Input:  001011    Output: 3
"""



class Solution:
	def numSetBits(self, A):
		ret = 0
		while A != 0:
			if A & 1:
				ret += 1
			A = A >> 1
		return ret


if __name__ == '__main__':
	A = 11
	sol = Solution()
	out = sol.numSetBits(A=A)
	temp = 0