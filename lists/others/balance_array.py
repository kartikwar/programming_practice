'''https://www.interviewbit.com/problems/balance-array'''


class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
		ans = 0
		if len(A) < 2:
			ans = len(A)
			return ans

		odd = sum([A[i] for i in range(1, len(A), 2)])
		even = sum([A[i] for i in range(0, len(A), 2)])
		carry_val = 0
		# counter = 0

		for ind, value in enumerate(A):
			if ind % 2 == 0:
				#if current index is even
				even = even - value + carry_val
			else:
				odd = odd - value + carry_val
			if odd == even:
				ans += 1
			carry_val = value
		return ans

			 


if __name__ == '__main__':
	sol = Solution()
	A =  [5,5,2,5,8]
	print(sol.solve(A))
