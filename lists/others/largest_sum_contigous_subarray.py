'''Maximum Subarray Sum'''


class Solution:
    """
    Returns the maximum subarray sum (Kadane's Algorithm).
    """

    def solve(self, A):
        max_sum = float('-inf')  # Handle all negative numbers correctly
        curr_sum = 0

        for num in A:
            curr_sum += num  # Add the current number

            # Update max_sum
            max_sum = max(max_sum, curr_sum)

            # Reset curr_sum if it goes below zero
            if curr_sum < 0:
                curr_sum = 0

        return max_sum


if __name__ == "__main__":
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    out = sol.solve(A=A)
    print(out)
