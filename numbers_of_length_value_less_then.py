# --------------------------------------------------------
# GO Jeck Assignment Solution File
# Written by Kartik Sirwani
# --------------------------------------------------------

class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A, B, C):
		out_array = []

		if B <= 0:
			return len(out_array)

		if B == 1:
			lowest_number = 0
			highest_number = 9
		
		if B > 1:
			number_of_zeros = B - 1
			lowest_number = ['0']*number_of_zeros
			lowest_number = '1' + ''.join([str(elem) for elem in lowest_number])
			highest_number = ['9']*B
			highest_number = ''.join([str(elem) for elem in highest_number])
		
		if int(highest_number) > C:
			highest_number = str(C)
		
		if int(highest_number) < C:
			highest_number = str(int(highest_number) + 1)
		
		possible_numbers = list(range(int(lowest_number), int(highest_number)))
		

		for poss_num in possible_numbers:
			append_status = True
			poss_digits = list(str(poss_num))
			# a = A.copy()
			for digit in poss_digits:
				if int(digit) not in A:
					append_status = False
					break
			if append_status:
				out_array.append(poss_num)

		return len(out_array)

if __name__ == "__main__":
	A = [ 1, 5, 6, 9 ]
	B = 2
	C = 6346
	sol = Solution()
	out = sol.solve(A, B, C)
	temp = 0