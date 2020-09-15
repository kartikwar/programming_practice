"""
Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value.
Report the minimum XOR value.
"""



class Solution:


	def findMinXor(self, A):
		s = sorted(A)
		minn = s[0] ^ s[1]
		for i in range(1, len(A)):
			if (s[i] ^ s[i - 1] < minn):
				minn = s[i] ^ s[i - 1]
		return minn

if __name__ == '__main__':
	A = [0,4,7,9]
	
	sol = Solution()
	out = sol.findMinXor(A=A)
	temp = 0