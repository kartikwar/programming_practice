'''
Given an integer array A of size N.You can pick B elements 
from either left or right end of the array A to get maximum 
sum. Find and return this maximum possible sum. 

NOTE: Suppose B = 4 and array A contains 10 elements then You 
can pick first four elements or can pick last four elements or 
can pick 1 from front and 3 from back etc . you need to return 
the maximum possible sum of elements you can pick.
'''


class Solution:

	def solve(self, A, B):
		if len(A) < 2:
			return sum(A)
		else:
			#first pass
			start = 0
			curr_sum = 0
			max_sum = 0
			max_sum = sum(A[:B])
			curr_sum = sum(A[:B])
			#second pass
			start  = B - 1
			end = len(A) -1
			while (end >= len(A) - B)  and start >= 0:
				curr_sum = curr_sum - A[start] + A[end]
				if curr_sum > max_sum:
					max_sum = curr_sum
				end = end - 1
				start = start - 1 
			return max_sum