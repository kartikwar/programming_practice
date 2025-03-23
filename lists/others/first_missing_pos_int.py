class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)

        # Swap elements to their correct positions
        i = 0
        while i < n:
            correct_pos = A[i] - 1  # Where A[i] should be
            if 1 <= A[i] <= n and A[i] != A[correct_pos]:  # Valid number and needs swapping
                A[i], A[correct_pos] = A[correct_pos], A[i]  # Swap
            else:
                i += 1  # Move to next number only when no swap is needed

        # Find first missing positive
        for i in range(n):
            if A[i] != i + 1:
                return i + 1

        return n + 1  # If all are in place, return n+1


if __name__ == '__main__':
    sol = Solution()
    A = [2, 1, 4, 3, 4, 5]
    print(sol.firstMissingPositive(A))  # Expected Output: 6
