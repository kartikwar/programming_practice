'''https://www.interviewbit.com/problems/next-similar-number'''
import sys


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        if len(A) == 1:
            return -1

        A = [int(i) for i in A]

        max_value = -sys.maxsize

        for i in range(len(A) - 1, -1, -1):
            if A[i] < max_value:

                for k in range(len(A)-1, i, -1):
                    if A[i] < A[k]:
                        A[i], A[k] = A[k], A[i]
                        A = A[:i+1] + sorted(A[i+1:])
                        break

                A = [str(i) for i in A]
                return ''.join(A)
            else:
                max_value = A[i]

        return -1


if __name__ == "__main__":
    A = '218765'
    sol = Solution()
    print(sol.solve(A))
