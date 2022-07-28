'''
Problem Description
 
 

Given an integer array A of size N.

You need to check that whether there exist a element which 
is strictly greater than all the elements on left of it and 
strictly smaller than all the elements on right of it.

If it exists return 1 else return 0.

NOTE:

Do not consider the corner elements i.e A[0] and A[N-1] 
as the answer.


Problem Constraints
3 <= N <= 105

1 <= A[i] <= 109



Input Format
First and only argument is an integer array A containing N integers.



Output Format
Return 1 if there exist a element that is strictly greater 
than all the elements on left of it and strictly  smaller than 
all the elements on right of it else return 0.



Example Input
Input 1:

 A = [5, 1, 4, 3, 6, 8, 10, 7, 9]
Input 2:

 A = [5, 1, 4, 4]


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:
	A[4] = 6 is the element we are looking for.
	All elements on left of A[4] are smaller than it and 
	all elements on right are greater.

Explanation 2:
	No such element exits.
'''


import sys
class Solution:
	# @param A : list of integers
	# @return an integer
	def perfectPeak(self, A):
		status = 0
		max_dp = [-1]*len(A)
		min_dp = [-1]* len(A)
		
		max_val = -sys.maxsize
		min_val = sys.maxsize
		
		for i, a in enumerate(A):
			if a > max_val:
				max_dp[i] = 1
				max_val = a
			else:
				max_dp[i] = 0
				
		for i in range(len(A)-1, -1, -1):
			a = A[i]
			if a < min_val:
				min_dp[i] = 1
				min_val = a
			else:
				min_dp[i] = 0
		
				
		for i in range(1, len(A) -1):
			if max_dp[i] & min_dp[i]:
				status = 1
				break
		
		return status

if __name__ == '__main__':
	sol = Solution()
	A = [ 9488, 25784, 5652, 9861, 31311, 8611, 1671, 7129, 28183, 2743, 11059, 4473, 7927, 21287, 2259, 7214, 32529 ]
	print(sol.perfectPeak(A))
