'''Given a large number represent in the form of an integer array A, 
where each element is a digit.

You have to find whether there exists any permutation of the array A 
such that the number becomes divisible by 60.

Return 1 if it exists, 0 otherwise.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def divisibleBy60(self, A):
        if len(A)==1 and A[0] == 0:
            return 1
        if len(A)<=2:
            if (6 in A) and (0 in A):
                return 1
            else:
                return 0
        if (0 in A) and (sum(A))%3 == 0:
            for i in A:
                if i%2 == 0:
                    return 1
        return 0

if __name__ == '__main__':
    sol = Solution()
    A = [4,8,0,1]
    print(sol.divisibleBy60(A))