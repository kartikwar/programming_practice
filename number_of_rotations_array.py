# --------------------------------------------------------
# GO Jeck Assignment Solution File
# Written by Kartik Sirwani
# --------------------------------------------------------

class Solution:
	# @param A : list of integers
	# @return an integer
	def search(self, A):
		number_of_rots = 0
		last = len(A) - 1
		start = 0
		next = None
		prev = None
		mid = None
		if A and len(A):
			mid = int((last + start)/2)
			if A[last] > A[start]:
				number_of_rots = start
				return start
			else:
				number_of_rots = 0
		return number_of_rots            

if __name__ == "__main__":
	# A = [ 0,1,2, 3, 4, 5 ]
	A = [5,0,1,2,3,4]
	# target = 9
	# C = 6346
	sol = Solution()
	out = sol.search(A)
	temp = 0