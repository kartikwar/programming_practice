'''
Problem Link:- https://www.interviewbit.com/problems/majority-element/
'''

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def majorityElement(self, A):
		n = len(A)
		maj_element = A[0]
		count = 1

		for i in A:
			if i == maj_element:
				count += 1
			else:
				count -= 1
			if count == 0:
				maj_element = i
				count += 1
		return maj_element


if __name__ == '__main__':
	sol = Solution()
	A = [1,3,1]
	sol.majorityElement(A)