'''https://www.interviewbit.com/problems/reorder-data-in-log-files'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def reorderLogs(self, A):
		digit_logs = []
		char_logs = []

		for log in A:
			if log.split('-')[1].isdigit():
				digit_logs.append(log)
			else:
				char_logs.append(log.split('-'))

		char_logs = sorted(char_logs, key=  lambda x: x[0])
		char_logs = sorted(char_logs, key=lambda x : x[1:])

		for i in range(len(char_logs)):
			char_logs[i] = '-'.join(char_logs[i])

		char_logs.extend(digit_logs)
		return char_logs

			 


if __name__ == '__main__':
	sol = Solution()
	A = ["dig1-8-1-5-1", "let1-art-can", "dig2-3-6", "let2-own-kit-dig", "let3-art-zero"]
	print(sol.reorderLogs(A))