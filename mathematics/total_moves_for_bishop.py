'''
Given the position of a Bishop (A, B) on an 8 * 8 chessboard.

Your task is to count the total number of squares that can be visited by 
the Bishop in one move.

The position of the Bishop is denoted using row and column number 
of the chessboard.'''


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        r,c = A, B
        top_left = min(r, c) - 1
        top_right = min(r-1, 8 - c)
        bottom_left = min(8-r, c-1)
        bottom_right = min(8-r, 8-c)

        return top_left + top_right + bottom_left + bottom_right