'''
Problem Link :- https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/
'''


class Solution:
	# @param A : list of integers
	# @param B : list of integers
	def merge(self, A, B):
		ptr1, ptr2 = 0, 0
		
		while ptr1 < len(A) and ptr2 < len(B):
			if B[ptr2] > A[ptr1]:
				while  ptr1 < len(A) and B[ptr2] > A[ptr1]:
					ptr1 = ptr1 + 1
				
				if ptr1 == len(A):
					while ptr2 < len(B):
						A.append(B[ptr2])
						ptr2 = ptr2 + 1
					ptr1 = len(A)
				
				else:
					A.insert(ptr1, B.pop(ptr2))
					ptr1 = ptr1 + 1
			
			else:
				A.insert(ptr1, B.pop(ptr2))
				ptr1 = ptr1 + 1

		return A

if __name__ == '__main__':
	A = [ -4, -3, 0 ]
	B = [ 2 ]

	sol = Solution()
	print(sol.merge(A, B))