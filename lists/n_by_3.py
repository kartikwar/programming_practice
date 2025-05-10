'''https://www.interviewbit.com/problems/n3-repeat-number/'''

import sys

class Solution:

	def pop_min_key(self, counts):
		min_val = sys.maxsize
		min_idx = None

		for key, val in counts.items():
			if val < min_val:
				min_val = val
				min_idx = key

		del counts[min_idx]

		return counts


	# @param A : tuple of integers
	# @return an integer
	def repeatedNumber(self, A):
		status = -1
		counts = {}
		for i in A:
			if i in counts:
				counts[i] += 1
			else:
				#check length of counts
				if len(counts.keys())==3:
					counts = self.pop_min_key(counts)
				
				counts[i] = 1

		# counts = self.pop_min_key(counts)

		# high_vals = list(counts.keys())

		# count_1 = 0
		# count_2 = 0

		for key, val in counts.items():
			counts[key] = 0


		for i in A:
			if i in counts:
				counts[i] += 1

		for key, val in counts.items():
			if val > len(A)/3:
				status = key
				break

		return status			 


if __name__ == '__main__':
	sol = Solution()
	A =  [ 1000441, 1000441, 1000994 ]
	print(sol.repeatedNumber(A))
