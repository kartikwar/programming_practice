'''problem link :- https://www.interviewbit.com/problems/pairs-with-given-xor/'''

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def solve(self, A, B):
		count = 0
		xor_map = {}
		for i in A:
			xor = i ^ B
			if xor in xor_map:
				xor_map[xor] = 1
			else:
				xor_map[i] = 0
		for num, freq in xor_map.items():
			count += freq
		return count

if __name__ == '__main__':
	sol = Solution()
	A	= [3, 6, 8, 10, 15, 50]
	B = 5 
	print(sol.solve(A, B))

