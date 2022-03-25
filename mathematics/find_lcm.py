"""Find Lowest Common Multiple of given two integers."""

class Solution:
    # @param A : integer
    # @param B : integer
     # @return an long

    def gcd(self,A,B):
        if B%A==0:
            return A 
        return self.gcd(B%A,A)
    def solve(self, A, B):
        x = max(A,B)
        y = min(A,B)
        g = self.gcd(x,y)
        return (A*B)//g


if __name__ == '__main__':
    sol = Solution()
    sol = sol.solve(4,6)
    print(sol)

