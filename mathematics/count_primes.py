'''https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/'''


import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [True] * (n)
        primes[0] = False
        primes[1] = False

        for i in range(int(n**0.5) + 1):
            if primes[i] == False:
                continue
            else:
                for num in range(i*i, n, i):
                    primes[num] = False

        return sum(primes)


if __name__ == "__main__":
    nums = 10
    sol = Solution()
    out = sol.countPrimes(nums)
    print(out)
