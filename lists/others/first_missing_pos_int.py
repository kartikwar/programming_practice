'''https://www.interviewbit.com/problems/first-missing-integer/'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        i = 0
        last_val = len(A) + 1
        while i < len(A):
            if A[i] > 0 and A[i] < last_val:
                # A[i] should be at A[i]-1
                if A[i] != A[A[i] -1]:
                    # print('swapping positions ' + str(i) + ' and ' + str(A[i] -1))
                    # print('list is ' + str(A))
                    # print(A[i])
                    # print(A[A[i]-1])
                    temp = A[i]
                    A[i] = A[A[i] - 1]
                    A[temp -1 ] = temp
                    i -= 1
            i+=1
        for i in range(len(A)):
            if A[i] != i + 1:
                return i + 1
        return last_val
        temp = 0

if __name__ == '__main__':
    sol = Solution()
    A = [3,4,-1,1]
    print(sol.firstMissingPositive(A))