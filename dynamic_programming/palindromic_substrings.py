'''
Given a string A consisting of only lowercase English letters.
Return the number of substrings of A which are palindrome.

Input 1:
A = "aba"

Output 1:
4

Explanation 1:
The plaindrome substrings are "a", "b", "a" and "aba".
'''


class Solution:
	
	def is_palindrome(self, i, j):
		# is_pali = 1
		if i> j:
			# self.dp[i][j] = 1
			return 1
		if self.dp[i][j] != -1:
			# already computed this substring, 
			# thus using memoization
			return self.dp[i][j]
		if self.A[i] != self.A[j]:
			self.dp[i][j] = 0
			# is_pali = 0
			return 0
		is_pali = self.is_palindrome(i+1, j-1)
		self.dp[i][j] = is_pali
		return is_pali
		# return self.dp[i][j]
	
	# @param A : string
	# @return an integer        
	def solve(self, A):
		count = 0
		dp = [[-1 for i in range(len(A))] for j in range(len(A))]
		self.dp = dp
		self.A = A

		#set all diagonal elements to 1
		for i in range(len(dp)):
			dp[i][i] = 1

		for i in range(len(A)):
			for j in range(i+1, len(A)):
				self.is_palindrome(i,j)
					# count += 1
		
		for i in range(len(dp)):
			for j in range(len(dp)):
				if dp[i][j] ==1:
					count += 1

		return count




if __name__ == '__main__':
	sol = Solution()
	print(sol.solve('fbrrb'))
