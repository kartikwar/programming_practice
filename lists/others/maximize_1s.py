class Solution:
	# @param A : string
	# @return a list of integers
	def flip(self, A):
		result = []
		left = None
		right = None
		normalized = []
		for ele in A:
			if ele =='0':
				normalized.append(1)
			else:
				normalized.append(-1)
		max_sum = 0

		for index, ele in enumerate(normalized):
			prev_max = max_sum
			curr_sum = sum(normalized[left:index]) + ele
			max_sum = max(ele, prev_max, curr_sum)
			
			if max_sum == prev_max:
				continue
			elif max_sum == ele:
				left, right = index, index
			else:
				right = index

		if left is not None:	
			result = [left +1, right +1]
		
		return result

if __name__ == '__main__':
	sol = Solution()
	A = "0111000100010"
	out = sol.flip(A)
	print(out)