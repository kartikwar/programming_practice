'''https://www.interviewbit.com/problems/potions/'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def minSmoke(self, A):
        n = len(A)
        s = [[0 for i in range(n)] for j in range(n)]
        dp = [[0 for i in range(n)] for j in range(n)]
            
        for i in range(n):
            s[i][i] = A[i]
        
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                minm = 1 << 30
                for k in range(i,j):
                    temp = dp[i][k] + dp[k + 1][j] + (s[i][k] * s[k + 1][j])
                    if (temp < minm):
                        s[i][j] = (s[i][k] + s[k + 1][j])%100
                        minm = temp
                        dp[i][j] = minm

        return dp[0][n - 1]

        # return min(smoke1, smoke2)


if __name__ == '__main__':
    # A = [ 10, 6, 7, 4, 5, 5, 3, 10, 3, 2, 4 ]
    # A = [40,60,20]
    A = [ 49, 85, 29, 85, 41, 93, 22, 28, 99, 87, 68, 72, 60, 90 ]
    sol = Solution()
    print(sol.minSmoke(A))