'''https://www.interviewbit.com/problems/word-break/'''


class Solution:
	# @param A : string
	# @param B : list of strings
	# @return an integer
	def wordBreak(self, A, B):
		s = A
		wordDict = B
		dp = [0] * (len(s) + 1)
		dp[len(s)] = 1

		for i in  range(len(s) -1 , -1, -1):
			for w in wordDict:
				if (i + len(w) <= len(s)) and s[i: i + len(w)] == w:
					dp[i] = dp[i+ len(w)]
				if dp[i]:
					break
		
		return dp[0]



if __name__ == '__main__':
	sol = Solution()
	A = "leetcodeleet"
	B = [ "code", "leet"]
	# A = "myinterviewtrainer"
	# B = ["trainer", "my", "interview"]
	# A = "a"
	# B = ["aaa"]

	print(sol.wordBreak(A, B))