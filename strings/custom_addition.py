# --------------------------------------------------------
# GO Jeck Assignment Solution File
# Written by Kartik Sirwani
# --------------------------------------------------------

class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A, B):
		A = [str(i) for i in A]
		B = [str(i) for i in B]
		numberA= int(''.join(A))
		numberB = int(''.join(B))
		
		sum = str(numberA + numberB)
		return [int(i) for i in sum]

if __name__ == "__main__":
	A = [ 1, 1 ]
	B = [1]
	# C = 6346
	sol = Solution()
	out = sol.solve(A, B)
	temp = 0