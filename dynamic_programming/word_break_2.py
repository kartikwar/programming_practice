
"""https://www.interviewbit.com/problems/word-break-ii/"""

# Another approach in Python3
def wordBreak(A, B):
	s = A
	Dict = B
	# code here
	l = len(s)
	dp = [0]*l

	# Here storing word which can be obtain from given index
	for i in range(l):
		arr = []
		for j in range(i+1, l+1):
			if( s[i:j] in Dict ):
				arr.append(s[i:j])
		dp[i] = arr
		                                                                                     
	# From bottom up aprroch form the string
	sol = [0]*l
	for i in range(l-1, -1, -1):
		ans = []
		if dp[i]:
			for word in dp[i]:
				# If word is last word in string directly append
				if( i+len(word) == l):
					ans.append(word)
					
				# Combine with each word present already and store
				elif( sol[i+len(word)] ):
					for w in sol[i+len(word)]:
						ans.append(word+" "+w)
		sol[i] = ans
	return sol[0]


# def wordBreak(A, B):
# 	n = 5
# 	return wordBreak_(n, A, B)
 
if __name__=='__main__':
	n = 5
	Dict = ["cats", "cat", "and", "sand", "dog"]
	s = "catsanddog"
	print(wordBreak(s, Dict))