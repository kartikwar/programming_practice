'''
Given a sorted array A and a target value B, 
return the index if the target is found. If not, 
return the index where it would be if it were 
inserted in order.

You may assume no duplicates in the array.
'''

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def searchInsert(self, A, B):
		
		start = 0
		end = len(A) -1
		found = False
		while start <= end:
			mid = (start + end)//2
			if B == A[mid]:
				found = True
				break
			if B > A[mid]:
				start = mid + 1
			else:
				end = end - 1
				
		if found:
			return mid
		else:
			 return start


if __name__ == '__main__':
	A = [ 1, 3, 5, 6 ]
	B = 7

	sol = Solution()
	print(sol.searchInsert(A, B))