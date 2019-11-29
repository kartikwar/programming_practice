class Solution:
	# @param A : list of integers
	# @return an integer
	def maxSpecialProduct(self, A):
		self.maxproduct = 0
		left_special = []
		right_special = []
		left_status = False
		right_status = False
		
		for i in range(1,len(A)):
			# temp  = 0
			# if i == 9:
			# 	temp = 0
			
			for j in range(i, -1, -1):
				if A[j] > A[i]:
					left_status = True
					if len(left_special):
						left_special.pop()
					left_special.append(j)
					break
			
			for k in range(i, len(A)):
				if A[k] > A[i]:
					right_status = True
					if len(right_special):
						right_special.pop()
					right_special.append(k)
					break
			
			if left_status and right_status:
				product = left_special[0] * right_special[0]
				if product > self.maxproduct:
					self.maxproduct = product
			
			left_status = False
			right_status = False

		
		return self.maxproduct % 1000000007

if __name__ == "__main__":
	A  = [5,9,6,8,6,4,6,9,5,4,9]
	# A = [ 7, 5, 7, 9, 8, 7 ]
	# A = [ 4, 6, 5, 5, 6, 6, 5, 6, 7, 5, 5, 7, 7 ]
	# A = [ 1950, 9417, 7760, 1939, 8551, 5184, 2187, 1097, 9686, 525, 7923, 364, 9182, 3013, 3252, 2203, 5496, 1537, 3455, 2209, 6981, 8032, 831, 2096, 6715, 3113, 2137, 9938, 2010, 5686, 2920, 4382, 9611, 9909, 1610 ]
	# A = [5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9 ]
	sol = Solution()
	out = sol.maxSpecialProduct(A)
	temp = 0