'''https://www.interviewbit.com/problems/order-of-people-heights/'''


class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return a list of integers
	def order(self, A, B):
		out = [0 for i in range(len(A))]
		available = list(range(len(A)))
		lookup = sorted(zip(A, B), key =lambda x:x[0])
		for obj in lookup:
			val = obj[0]
			freq = obj[1]
			pos = available.pop(freq)
			out[pos] = val
		return out


if __name__ == '__main__':
	sol = Solution()
	A = [5, 3, 2, 6, 1, 4]
	B =  [0, 1, 2, 0, 3, 2]
	sol.order(A,B)