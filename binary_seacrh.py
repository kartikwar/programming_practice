# --------------------------------------------------------
# GO Jeck Assignment Solution File
# Written by Kartik Sirwani
# --------------------------------------------------------

class Solution:
	# @param A : list of integers
	# @return an integer
	def search(self, A, target):
		# A = sorted(A)

		n = len(A)

		start = 0

		end = n -1

		while start <= end :
			mid = int((start + end) /2) 
			
			if A[mid] == target:
				return mid

			elif A[mid] < target:
				start = mid + 1

			else:
				end = mid -1            

if __name__ == "__main__":
	A = [ 1, 2 , 3, 4, 5, 6, 7, 8, 9, 10 ]
	target = 9
	# C = 6346
	sol = Solution()
	out = sol.search(A, target)
	temp = 0