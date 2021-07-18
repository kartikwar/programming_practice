# --------------------------------------------------------
# GO Jeck Assignment Solution File
# Written by Kartik Sirwani
# --------------------------------------------------------

class Solution:
	# @param A : list of integers
	# @return an integer
	
	# Recursive Python function to solve the tower of hanoi
	
	def fibonacci(self, n):
		if n < 0:
			return "incorrect input"
		if n < 2:
			return n
		else:
			return self.fibonacci(n-1)  + self.fibonacci(n-2)
	# Driver code
	# n = 4
	# TowerOfHanoi(n, 'A', 'B', 'C')


# A, C, B are the name of rods

# Contributed By Dilip Jain


if __name__ == "__main__":
	sol = Solution()
	out = sol.fibonacci(6)
	temp = 0