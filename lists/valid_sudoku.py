"""Probkem Link :- https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/"""

import unittest


class Solution:
    def isValidSudoku(self, board) -> bool:
        status = True
        rows = {}
        columns = {}
        squares = {}

        for i in range(len(board)):
            rows[i] = rows.get(i, set())
            for j in range(len(board[0])):
                columns[j] = columns.get(j, set())
                num = board[i][j]

                if num == ".":
                    continue

                square_index = (i//3, j//3)
                squares[square_index] = squares.get(square_index, set())

                if (num in rows[i]) or (num in columns[j]) or (num in squares[square_index]):
                    status = False
                    return status

                rows[i].add(num)
                columns[j].add(num)
                squares[square_index].add(num)

        return status


class TestSudokuValidation(unittest.TestCase):
    def test_valid_board(self):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        s = Solution()
        self.assertTrue(s.isValidSudoku(board))


if __name__ == "__main__":
    unittest.main()
