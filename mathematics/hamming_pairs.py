'''https://www.interviewbit.com/problems/sum-of-pairwise-hamming-distance/'''
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def hammingDistance(self, A):
		n = len(A)
		ans = 0
		l = 1000000007
		for i in range(32):
			count1 = 0
			count0 = 0
			for j in range(n):
				if ((1<<i) & A[j]) == 0:
					count0 += 1
				else:
					count1 += 1
			ans += (count0 * count1 * 2) % l
		return ans % l

if __name__ == '__main__':
	sol = Solution()
	A = [2, 4, 6]
	sol.hammingDistance(A)