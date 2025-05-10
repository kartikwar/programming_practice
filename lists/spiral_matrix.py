'''
See problem description at:- https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
'''

class Solution:

	def generate_matrix(self):
		result = []
		result = [[-1 for i in range(self.C)] for j in range(self.B) ]
		for row in range(self.B):
			start_index = row * self.C
			end_index = start_index + self.C
			result[row] = self.result[start_index:end_index]
		return result

	def generate_spiral(self):
		spiral = []
		result = self.result
		dir = 0
		top, down, left, right = 0, self.B - 1, 0, self.C - 1
		while (top <= down) and (left <= right):
			if dir == 0:
				for i in range(left, right +1):
					spiral.append(result[top][i])
				top += 1
			elif dir == 1:
				for i in range(top, down + 1):
					spiral.append(result[i][right])
				right -= 1
			elif dir == 2:
				for i in range(right, left-1, -1):
					spiral.append(result[down][i])
				down -= 1
			else:
				for i in range(down, top-1, -1):
					spiral.append(result[i][left])
				left += 1

			dir = (dir + 1) % 4
		return spiral		
	
	# @param A : list of integers
	# @param B : integer
	# @param C : integer
	# @return a list of list of integers
	def solve(self, A, B, C):
		# result = A
		self.result = A
		self.B = B
		self.C = C
		self.result = self.generate_matrix()
		self.result = self.generate_spiral()
		self.result = self.generate_matrix()
		return self.result

if __name__ == '__main__':
	sol = Solution()
	A = [1,2,3,4,5,6,7,8,9]
	B = 3
	C = 3
	out = sol.solve(A, B, C)
	temp = 0
