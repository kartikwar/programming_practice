'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will 
only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
'''

class Solution:
	def transpose(self, A):
		max_steps = len(A)
		for i in range(max_steps):
			for j in range(i,len(A)):
				A[i][j], A[j][i] = A[j][i], A[i][j]
		return A
	
	def swap_cols(self, A):
		for row in range(len(A)):
			start = 0
			end = len(A) -1
			while start <= end:
				A[row][start], A[row][end] = A[row][end], A[row][start]
				start += 1
				end -= 1
		return A

	# @param A : list of list of integers
	# @return the same list modified
	def rotate(self, A):
		A = self.transpose(A)		
		A = self.swap_cols(A)
		# A= self.transpose(A)
		return A


if __name__ == '__main__':
	sol = Solution()
	A = [[1,2,3], [4,5,6], [7,8,9]]
	# A = [[1,2], [3,4]]
	sol.rotate(A)