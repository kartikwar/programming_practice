'''https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/'''


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Avoid unnecessary full rotations
        count = 0  # Number of elements moved

        for start in range(n):
            if count >= n:
                break

            current = start
            prev = nums[start]

            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break


if __name__ == "__main__":
    nums = [-1, -100, 3, 99]
    k = 2
    sol = Solution()
    out = sol.rotate(nums, k)
    print(nums)
