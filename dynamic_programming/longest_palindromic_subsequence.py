'''
Problem Link:- https://www.interviewbit.com/problems/longest-palindromic-subsequence/
'''


class Solution:
	
	def max_palindrome(self, i, j):
		if self.dp[i][j] != -1:
			return self.dp[i][j]

		if j-i == 0:
			self.dp[i][j] = 1
			# return self.dp[i][j]
		elif j-i==1:
			if self.A[i] == self.A[j]:
				self.dp[i][j] = 2
			else:
				self.dp[i][j] = 1
			# return self.dp[i][j]
		else:
			if self.A[i] == self.A[j]:
				self.dp[i+1][j-1] = self.max_palindrome(i+1, j-1)
				self.dp[i][j] = 2 + self.dp[i+1][j-1]
			else:
				self.dp[i+1][j] = self.max_palindrome(i+1, j)
				self.dp[i][j-1] = self.max_palindrome(i,j-1)
				self.dp[i][j] = max(self.dp[i+1][j], self.dp[i][j-1])
		# self.dp[j][i] = self.dp[i][j]
		
		return self.dp[i][j]
	
	# @param A : string
	# @return an integer        
	def solve(self, A):
		dp = [[-1 for i in range(len(A))] for j in range(len(A))]
		self.dp = dp
		self.A = A

		# for i in range(len(A)):
		# 	self.dp[i][i] = 1

		for i in range(len(A)):
			for j in range(i, len(A)):
				self.max_palindrome(i,j)
					# count += 1
		
		
		return self.dp[0][len(A)-1]

if __name__ == '__main__':
	sol = Solution()
	print(sol.solve('agbdba'))