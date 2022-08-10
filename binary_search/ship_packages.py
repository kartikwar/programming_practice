'''Problem Link :- https://www.interviewbit.com/problems/capacity-to-ship-packages-within-b-days/ '''

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def split_packages(self, A, target, B):
		days = 0

		if len(A):
			curr_sum = A[0]

			for i in range(1, len(A)):
				if curr_sum + A[i] < target + 1:
					curr_sum = curr_sum + A[i]
				else:
					days += 1
					curr_sum = A[i]

			days = days + 1

		if days < B + 1:
			return True

		else:
			return False

	def solve(self, A, B):
		low = max(A)
		high = sum(A)
		min_capacity = high

		while low <= high:
			mid = (low + high)//2
			target = mid
			possible = self.split_packages(A, target, B)

			if possible:
				min_capacity = mid
				high = mid-1

			else:
				low = mid + 1

		return min_capacity


if __name__ == '__main__':
	A = [ 11, 2, 19, 15, 6, 14, 9, 5, 14, 8, 13, 14, 18, 3, 9, 4, 4, 16, 6, 7, 10, 10, 11, 13, 10, 3, 9, 9 ]
	B = 15

	sol = Solution()
	print(sol.solve(A, B))