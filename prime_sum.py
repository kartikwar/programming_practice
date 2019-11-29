import math


class Solution:
    def primesum(self, n: int) -> 'List[int]':
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False

        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i * 2, n + 1, i):
                    is_prime[j] = False

        for i in range(2, n):
            if is_prime[i] and is_prime[n - i]:
                return [i, n - i]

        return []