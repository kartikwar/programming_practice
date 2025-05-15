'''https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/'''


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 -
                                        j] = matrix[i][n - 1 - j], matrix[i][j]


if __name__ == "__main__":
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol = Solution()
    out = sol.rotate(nums)
    print(nums)
