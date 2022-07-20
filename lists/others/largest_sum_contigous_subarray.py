class Solution:
	"""
	returns smallest sum
	"""
	def solve(self, A):
		curr_sum = 0
		max_sum = 0
		start = -1
		end = -1
		mstart = -1
		mend = -1

		for i in range(len(A)):
			curr_sum = curr_sum + A[i]

			if curr_sum > 0:
				if start ==-1:
					start = i

			if curr_sum > max_sum:
				end = i
				mstart = start
				mend = end
				max_sum = curr_sum
			
			if curr_sum < 0:
				start = -1
				end = -1
				curr_sum = 0

		return max_sum, start, end




if __name__ == "__main__":
	A = [3, 4, 2, -3, -1, 7, -5]
	# A = [1, -1, -1, -1, 1,1,1,-1,1,1,1,-1,1]
	# A = []
	sol = Solution()
	out, start_index, end_index = sol.solve(A=A)
	print(out)