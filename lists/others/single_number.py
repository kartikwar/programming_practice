'''https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/'''


class Solution:
    def singleNumber(self, nums):
        if not nums:
            return None
        result = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            result = result ^ num
        return result


if __name__ == '__main__':
    sol = Solution()
    nums = [4, 1, 2, 1, 2]
    print(sol.singleNumber(nums))
