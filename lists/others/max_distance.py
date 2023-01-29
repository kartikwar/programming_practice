'''https://www.interviewbit.com/problems/max-distance/hints/'''
import sys
class Solution:
    # @param A : list of integers
    # @return an integer
    def maximumGap(self, A):
        ans = -sys.maxsize
        for i in range(len(A)):
            A[i] = (i, A[i])
        A = sorted(A, key=lambda x: x[1])
        max_indexes = [-1]* len(A)
        max_ind = -sys.maxsize
        for i in range(len(A)-1, -1, -1):
            max_ind = max(max_ind, A[i][0])
            max_indexes[i] = max_ind
            # max_ind = max_indexes            
        for i in range(len(A)):
            ans = max(max_indexes[i]-A[i][0], ans) 
        return ans


if __name__ == '__main__':
    sol = Solution()
    A = [ 1, 10 ]
    print(sol.maximumGap(A))