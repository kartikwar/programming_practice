'''https://www.interviewbit.com/problems/balance-array'''


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def solve(self, A):
		ans = 0
		suffix = [0] * len(A)

		for i in range(len(suffix)-1, -1, -1):
			if i + 2 < len(A):
				suffix[i] = A[i] + suffix[i+2]
			else:
				suffix[i] = A[i]
		
		odd, even = 0, 0

		for i in range(len(A)):

			if i + 1 < len(A):
				suffix_1 = suffix[i+1]
			else:
				suffix_1 = 0
			
			if i + 2 < len(A):
				suffix_2 = suffix[i+2]
			else:
				suffix_2 = 0

			if (i + 1) % 2 == 0:
				even_term = suffix_2 + even
				odd_term = suffix_1 + odd
			else:
				even_term = suffix_1 + even
				odd_term = suffix_2 + odd

			if even_term == odd_term:
				ans +=1
			if i % 2 == 0:
				even += A[i]
			else:
				odd += A[i]

		return ans

			 


if __name__ == '__main__':
	sol = Solution()
	A =  [5,5,2,5,8]
	print(sol.solve(A))
