'''
Given an integer array A, move all 0's to the end 
of it while maintaining the relative order of the 
non-zero elements.


Note that you must do this in-place without making 
a copy of the array.

Problem Constraints
1 <= |A| <= 105

Input Format
First argument is array of integers A.

Output Format
Return an array of integers which satisfies above property.


Example Input

Input 1:
A = [0, 1, 0, 3, 12]

Input 2:
A = [0]


Example Output

Ouput 1:
[1, 3, 12, 0, 0]

Ouput 2:
[0]
'''

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def solve(self, A):
		space = 0
		for i in range(0, len(A)):
			if A[i] == 0:
				space += 1
			else:
				A[i], A[i-space] = A[i-space], A[i]

		return A

if __name__ == '__main__':
	sol = Solution()
	A = [0,1,0,3,12]
	sol.solve(A)
