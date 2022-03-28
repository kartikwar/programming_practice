"""

Given a bitonic sequence A of N distinct elements, write a program to find a 
given element B in the bitonic sequence in O(logN) time.

NOTE:

A Bitonic Sequence is a sequence of numbers which is first 
strictly increasing then after a point strictly decreasing.
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        start = 0
        end = len(A) - 1

        while start <= end:
            mid = (start + end)//2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                #check mid -1 isless then A[mid]
                if A[mid-1] < A[mid]:
                    start = mid + 1
                else:
                    end = mid -1
            else:
                #check mid + 1 is greater then A[mid]
                if A[mid-1] < A[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        
        return -1

if __name__ == '__main__':
    sol = Solution()
    A = [ 1, 20, 50, 40, 10 ]
    B = 5
    print(sol.solve(A, B))