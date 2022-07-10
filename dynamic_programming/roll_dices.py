'''
You rolled a dice K times and got a sum of A after summing all the values you got after a roll.
Find the number of ways you could have got a sum of A after rolling K times, since this value can be very large return modulo 109+7.


Problem Constraints
1 <= A <= 106


Input Format
Given an integer A.


Output Format
Return and integer.


Example Input
Input 1:
A = 2
Input 2:

A = 3


Example Output
Output 1:
2
Output 2:

4


Example Explanation
Explanation 1:
Ways to get sum 2 are {1, 1} {2}.
Explanation 2:

Ways to get sum 3 are {1, 1, 1}, {1, 2}, {2, 1}, {3}
'''


class Solution:
    # @param A : integer
    # @return an integer
    
    def findWays(self, N, dp):
    
        # Base Case
        if (N == 0):
            return 1
        
        # Return already
        # stored result
        if (dp[N] != -1):
            return dp[N]
    
        cnt = 0
    
        # Recur for all 6 states
        for i in range (1, 7):
            if (N - i >= 0):
                cnt = (cnt + self.findWays(N - i, dp))
    
        # Return the result
        dp[N] = cnt
        return dp[N]
    
    def solve(self, A):
        dp = [-1]* (A+1)
        return self.findWays(A, dp)


if __name__ == '__main__':
    sol = Solution()
    print(sol.solve(4))