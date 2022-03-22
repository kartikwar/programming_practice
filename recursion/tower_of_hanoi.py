# --------------------------------------------------------
# GO Jeck Assignment Solution File
# Written by Kartik Sirwani
# --------------------------------------------------------

class Solution:
	# @param A : list of integers
	# @return an integer
	
	# Recursive Python function to solve the tower of hanoi
	
	def TowerOfHanoi(self, n, source, destination, auxiliary):
		if n == 1:
			print("Move disk 1 from source", source, "to destination", destination)
			return
		self.TowerOfHanoi(n - 1, source, auxiliary, destination)
		print("Move disk", n, "from source", source, "to destination", destination)
		self.TowerOfHanoi(n - 1, auxiliary, destination, source)
	
	# Driver code
	# n = 4
	# TowerOfHanoi(n, 'A', 'B', 'C')


# A, C, B are the name of rods

# Contributed By Dilip Jain


if __name__ == "__main__":
	# A = [ 1, 2 , 3, 4, 5, 6, 7, 8, 9, 10 ]
	target = 9
	# C = 6346
	sol = Solution()
	out = sol.TowerOfHanoi(4, 'A' , 'B', 'C')
	temp = 0