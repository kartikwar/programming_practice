'''Given an integer A.
Swap the Bth and Cth bit from right in binary representation of A.
Return the integer formed.
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        bits = format(A, 'b')

        bits = bits.zfill(max(B,C))

        bits = list(bits)

        temp = bits[-B]
        bits[-B] = bits[-C]
        bits[-C] = temp

        bits = ''.join(bits)
        
        return int(bits, 2)


if __name__ == '__main__':
    A = 5
    B = 1
    C = 2
    sol = Solution()
    print(sol.solve(A, B, C))