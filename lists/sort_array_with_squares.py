'''
Problem Description

Given a sorted array A containing N integers 
both positive and negative.

You need to create another array containing the 
squares of all the elements in A and return 
it in non-decreasing order.

Try to do this in O(N) time.


Problem Constraints
1 <= N <= 105.

-103 <= A[i] <= 103



Input Format
First and only argument is an 
integer array A.



Output Format
Return a integer array as described 
in the problem above.

Example Input
Input 1:
A = [-6, -3, -1, 2, 4, 5]

Example Output
Output 1:
A = [1, 4, 9, 16, 25, 36]

Solution Approach: try to use merge sort concept
'''


class Solution:
	# @param A : list of integers
	# @return a list of integers
	def solve(self, A):
		left_array = []
		right_array = []
		for ele in A:
			if ele <0:
				left_array.append(ele)
			else:
				right_array.append(ele)
		
		#apply merge sort algo here
		i = 0
		j = 0
		k = 0

		left_array = left_array[::-1]

		while i < len(left_array) and j < len(right_array):
			if -left_array[i] <  right_array[j]:
				A[k] = left_array[i]
				i += 1
			else:
				A[k] = right_array[j]
				j += 1
			k += 1

		while i < len(left_array):
			A[k] = left_array[i]
			i += 1
			k += 1
		
		while j < len(right_array):
			A[k] = right_array[j]
			j += 1
			k += 1

		A = [a*a for a in A]

		return A

if __name__ == '__main__':
	sol = Solution()
	A = [-6, -3, -1, 2, 4, 5]
	print(sol.solve(A))