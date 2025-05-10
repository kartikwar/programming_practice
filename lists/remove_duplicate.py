'''Problem Link:- https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/'''


class Solution:
    # @param A : list of integers
    # @return an integer

    def removeDuplicates(self, nums):
        if not nums:
            return 0
        j = 0
        for k in range(1, len(nums)):
            if nums[k] != nums[j]:
                j += 1
                nums[j] = nums[k]
        return j + 1


if __name__ == '__main__':
    A = [1, 1, 2]
    sol = Solution()
    print(sol.removeDuplicates(A))
