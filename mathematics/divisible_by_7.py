class Solution:
    # @param A : integer
    # @param B : integer
     # @return an long
    def solve(self, A, B):
        if A %7 == 0:
            a = A
        else:
            a = (A//7 + 1)* 7 
        last = ((B)//7)*7
        n = (last - a)//7 + 1
        result = (n) * (2*a + (n-1) * 7)
        return int(result//2)

if __name__ == '__main__':
    sol = Solution()
    out = sol.solve(99,115)
    print(out)