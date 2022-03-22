import math

class Solution:
	# @param A : list of integers
	# @return an integer
	def is_prime(self, A):
		prime = True
		if A <= 1:
			prime = False
			return prime
		if A == 2:
			prime = True
			return prime
		for i in range(2, int(math.sqrt(A)) + 1):
			if A % i == 0:
				prime = False
				break
		return prime

	def primesum(self,A):
		for i in range(A):
			if self.is_prime(i):
				if self.is_prime(A-i):
					return [i, A-i]

if __name__ == "__main__":
	A = 8
	sol = Solution()
	out = sol.primesum(A)
	temp = 0