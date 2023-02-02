'''https://www.interviewbit.com/problems/maximum-unsorted-subarray/'''
import sys
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def subUnsort(self, A):
		min_index = sys.maxsize
		max_index = -sys.maxsize
		for i in range(len(A) -1 ):
			if A[i+ 1] < A[i]:
				min_index = min(min_index, i)
				max_index = max(max_index, i + 1)
		if min_index != sys.maxsize:
			
			min_val = sys.maxsize
			max_val = -sys.maxsize

			for i in range(min_index,max_index + 1):
				min_val = min(min_val, A[i])
				max_val = max(max_val, A[i])

			for i in range(0, min_index):
				if A[i] > min_val:
					min_index = i
					break
			for i in range(len(A)-1, max_index, -1):
				if A[i] < max_val:
					max_index = i
					break
			return [min_index, max_index]			
		else:
			return [-1]


if __name__ == '__main__':
	sol = Solution()
	A = [ 4, 15, 4, 4, 15, 18, 20 ]
	print(sol.subUnsort(A))