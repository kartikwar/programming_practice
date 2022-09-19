'''https://www.interviewbit.com/problems/distinct-numbers-in-window/'''

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):
		out = []
		counter = {}

		batch = A[0:B]

		for i in batch:
			if i  in counter:
				counter[i] += 1
			else:
				counter[i] = 1

		out.append(len(counter))

		for i in range(1, len(A) - B + 1):
			prev = A[i-1]
			counter[prev] -= 1

			if not counter[prev]:
				counter.pop(prev)

			last_ind = i + B -1

			if A[last_ind] in counter:
				counter[A[last_ind]] += 1
			else:
				counter[A[last_ind]] = 1

			count = len(counter)

			# batch = A[i:i +B]
			# count = len(set(batch))
			out.append(count)
		return out


if __name__ == '__main__':
	sol = Solution()
	A = [1, 2, 1, 3, 4, 3]
	B = 3
	sol.dNums(A, B)