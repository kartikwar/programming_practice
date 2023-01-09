'''h1ttps://www.interviewbit.com/problems/n3-repeat-number/'''


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def repeatedNumber(self, A):
		tracker = []
		counts = []
		for num in A:
			if num in tracker:
				index = tracker.index(num)
				counts[index] +=1
			else:
				if len(tracker) < 2:
					tracker.append(num)
					counts.append(1)
				else:
					num_idx = 0

					while num_idx < len(tracker):
					# for num_idx in range(len(tracker)):
						counts[num_idx] -=1

						if counts[num_idx] == 0:
							tracker.pop(num_idx)
							counts.pop(num_idx)
						
						else:
							num_idx += 1

					if len(tracker) <2:
						tracker.append(num)
						counts.append(1)
		# temp = 0

		if len(tracker):
			# if len(tracker) <2:
			# 	tracker.append(None)

			counts = [0 for i in range(len(tracker))]

			for idx in range(len(tracker)):
				for ele in A:
					if ele == tracker[idx]:
						counts[idx] += 1

			for idx in range(len(counts)):
				ele = tracker[idx]
				count = counts[idx]

				if count > len(A)/3:
					return ele

			else:
				return -1

		else:
			return -1

			 


if __name__ == '__main__':
	sol = Solution()
	A =  [ 1, 1, 1, 2, 3, 5, 7 ]
	print(sol.repeatedNumber(A))
