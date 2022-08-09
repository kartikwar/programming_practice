class Solution:
	# @param A : list of strings
	# @return a list of strings
	def specialStrings(self, A):
		results = []
		if len(A):
			for word in A:
				letters = list(word)
				if len(results) == 0:
					results = letters
				else:
					new_result = []
					for res in results:
						for letter in letters:
							new_result.append(res + letter)
					results = new_result		 
		else:
			results = A
		return results

if __name__ == '__main__' :
	sol = Solution()
	A = [ "yhf", "k" ]
	ans = sol.specialStrings(A)
	print(ans)