"""
The n-queens puzzle is the problem of placing n queens on 
an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens’ placement, 
where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        board = [['.']*A for _ in range(A)]

        # check if a queen already exists on board 
        # at the same row, same column or is diagonal
        # to already placed queens on the board
        def check(x,y,board):
            for i in range(A):
                for j in range(A):
                    if board[i][j]=='Q':
                        if i==x or j==y or (x-y)==(i-j) or (x+y)==(i+j):
                            return False
            return True
        
        def solve(board,row, ans):
            if row==A:
                to_append = [''.join(sa) for sa in board]
                ans.append(to_append)
                return
        
            for column in range(A):
                # function to check if its safe to place a queen at 
                # position (row, column)
                if check(row,column,board):
                    #if its safe place a queen
                    board[row][column] = 'Q'
                    # since one queen was placed at row,
                    # now place it at row + 1
                    solve(board,row+1,ans)
                    #if no combinations are possible, set position as empty
                    board[row][column] = '.'
        
        #a list changes in place so good to store structure,
        #in case you want a structure to change in each fn call,
        #use slicing or list.copy()
        ans = list()
        solve(board,0,ans)
        return ans

if __name__ == '__main__' :
    sol = Solution()
    ans = sol.solveNQueens(A=4)
    print(ans)