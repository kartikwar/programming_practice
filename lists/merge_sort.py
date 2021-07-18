import math

class Solution:
	# @param A : list of integers
	# @return a list of integers

	def merge(self, X, y, x):
		i = j = k = 0
		# while i < len()
		# Copy data to temp arrays L[] and R[] 
		# while i < len(X) and j < len(y): 
		# 	if X[i] < y[j]: 
		# 		x[k] = X[i] 
		# 		i+=1
		# 	else: 
		# 		x[k] = y[j] 
		# 		j+=1
		# 	k+=1
				
		return sorted(X +y)

	def sort(self, x):

		if len(x) > 1:
		
			mid = int(len(x)/2)
			
			X, y = x[:mid], x[mid:]

			# if len(X) == 1 and len(y) ==1:
			# 	temp = self.organize(X, y)
			# 	return self.organize(X, y)
		

		else:
			return x

		B = self.merge(self.sort(X), self.sort(y), x)
		
		return B

	def solve(self, A):
		mid = int(len(A)/2)

		if A and len(A):

			A = self.sort(A)
			# return sorted(A)
			# Traverse through 1 to len(A) 
			# for i in range(1, len(A)): 

    

		return A

if __name__ == "__main__":
	A = [9, 6,2, 1, 7, 8, 5]

	# A = []
	sol = Solution()
	out = sol.solve(A=A)
	pass