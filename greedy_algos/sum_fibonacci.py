'''https://www.interviewbit.com/problems/sum-of-fibonacci-numbers/'''
class Solution:
	# @param A : integer
	# @return an integer
	def fibsum(self, A):
		ans = 0
		v = [1,1]

		i = 2

		val = v[0] + v[1]

		while val < A + 1:
			val = v[i-1] + v[i-2]
			v.append(val)
			i  += 1

		remaining = A

		for i in range(len(v)-1, -1, -1):
			if v[i] <= remaining:
				remaining = remaining - v[i]
				ans += 1

			if remaining == 0:
				return ans



if __name__ == '__main__':
	sol = Solution()
	A = 10
	sol.fibsum(A)