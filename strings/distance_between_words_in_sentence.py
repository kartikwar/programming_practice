import math
import sys

class Solution: 
	"""
	returns distance b/w words in a sentence
	"""
	def solve(self, A, word1, word2):
		min_distance = sys.maxsize
		
		if A and len(A):
			
			all_words = list(A.split(" "))

			word1_indexes = [index for index, val in enumerate(all_words) if val == word1 ]
			word2_indexes = [index for index, val in enumerate(all_words) if val == word2 ]
		
		

		# if len(word1_indexes) and len(word2_indexes):
		# 	# 
		# 	for index1, index2 in zip(word1_indexes, word2_indexes):
		# 		distance = abs(index2 - index1) - 1
		# 		if distance < min_distance:
		# 			min_distance = distance 

		for index1 in word1_indexes:
			for index2 in word2_indexes:
				distance = abs(index1 - index2) - 1
				
				if distance < min_distance:
					min_distance = distance


				# temp = val

		 
		return min_distance

	def minimum_distance(self, A, word1, word2):
		min_dist = sys.maxsize

		if A and len(A):
			all_words = list(A.split(" "))
			
			word1_occurences = []
			
			word2_occurences = []

			for i, word in enumerate(all_words):
				
				if word == word1:
					word1_occurences.append(i)
					if len(word2_occurences):
						dist = abs(word2_occurences[-1] - i) -1 
						if dist< min_dist:
							min_dist = dist
				
				if word == word2:
					word2_occurences.append(i)
					if len(word1_occurences):
						dist = abs(word1_occurences[-1] - i) -1
						if dist< min_dist:
							min_dist = dist 
		
		return min_dist


if __name__ == "__main__":
	A = "the quick the brown quick brown the frog"
	# A = []
	sol = Solution()
	out = sol.minimum_distance(A=A, word1='quick', word2='frog')
	pass