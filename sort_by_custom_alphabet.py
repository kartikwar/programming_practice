# --------------------------------------------------------
# GO Jeck Assignment Solution File
# Written by Kartik Sirwani
# --------------------------------------------------------

class Solution:
	
	def compute_key(self, word):
		key_list = []
		for char in word:
			key_list.append(self.index_hash[char])
		return  key_list
	
	# @param A : list of integers
	# @return an integer
	def solve(self, A, B):
		
		index_hash = {}
		
		for ind, char in enumerate(B):
			index_hash[char] = ind

		self.index_hash = index_hash
		
		
		A = sorted(A, key=lambda a  : self.compute_key(a))
		
		return A

if __name__ == "__main__":
	A = ['home', 'oval', 'cat', 'egg', 'network', 'green']
	B = 'bcdfghijklmnpqrstvwxzaeiouy'
	# C = 6346
	sol = Solution()
	out = sol.solve(A, B)
	temp = 0