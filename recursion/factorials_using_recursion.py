# --------------------------------------------------------
# GO Jeck Assignment Solution File
# Written by Kartik Sirwani
# --------------------------------------------------------

class Solution:
	# @param A : list of integers
	# @return an integer
	
	# Recursive Python function to solve the tower of hanoi
	
	def factorial(self, n):
		if n < 0:
			return "incorrect input"
		if n < 2:
			return n
		else:
			return n * self.factorial(n-1)
	# Driver code
	# n = 4
	# TowerOfHanoi(n, 'A', 'B', 'C')


# A, C, B are the name of rods

# Contributed By Dilip Jain


if __name__ == "__main__":
	sol = Solution()
	out = sol.factorial(5)
	temp = 0