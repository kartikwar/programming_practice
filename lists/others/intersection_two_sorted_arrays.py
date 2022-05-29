# --------------------------------------------------------
# GO Jeck Assignment Solution File
# Written by Kartik Sirwani
# --------------------------------------------------------

class Solution:
	# @param A : list of integers
	# @return an integer
	def inter_two_arrays(self, A, B):
		hash_map = {}
		
		intersection =  []
		
		for i, val in enumerate(A):
			hash_map[val] = i
		
		for val in B:
			if val in hash_map.keys():
				intersection.append(val)
		return intersection
	
	def union_two_arrays(self, A, B):
		hash_map = {}
		
		intersection = []
		
		for i, val in enumerate(A):
			hash_map[val] = i
		
		for val in B:
			if val not in hash_map.keys():
				intersection.append(val)
		return A + intersection


if __name__ == "__main__":
	A = [ 1, 2, 4, 6, 10]
	B = [2, 4, 5, 7, 10]
	# target = 9
	# C = 6346
	sol = Solution()
	out = sol.inter_two_arrays(A, B)
	out2 = sol.union_two_arrays(A, B)
	temp = 0