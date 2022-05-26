'''
Given a range [A, B], find sum of integers divisible by 7 in this range.


Problem Constraints
1 <= A <= B <= 109


Input Format
First argument is an integer A.
Second argument is an integer B.


Output Format
Return an integer.


Example Input
Input 1:
A = 1
B = 7
Input 2:
A = 99
B = 115


Example Output
Output 1:
7
Output 2:
217
'''


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