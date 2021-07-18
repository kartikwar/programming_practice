import math

class Solution:

	"""
	returns true if balanced, else false
	"""
	def solve(self, A):
		balanced_status = False

		possible_starting = ['(', '{', '[']

		possible_closing = [')', '}', ']']

		relations = {
			'(' : ')',
			'{' : '}',
			'[' : ']'
		}		

		starting_brackets = []

		closing_brackets = []


		for char in A:
			if char in possible_starting:
				starting_brackets.append(char)
			
			if char in possible_closing:
				closing_brackets.append(char)
				
				if len(starting_brackets):
					if relations[starting_brackets[-1]] == char:
						starting_brackets.pop()
						closing_brackets.pop()
					else:
						break
				else:
					break
				# closing_brackets.append(char)

		if not len(starting_brackets) and not len(closing_brackets):
			balanced_status = True 

		return balanced_status


if __name__ == "__main__":
	A = '[(])'
	# A = []
	sol = Solution()
	out = sol.solve(A=A)
	pass