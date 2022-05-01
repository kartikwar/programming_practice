'''
You are given a 1D integer array B containing A integers.

Count the number of ways to split all the elements of the array into 3 
contiguous parts so that the sum of elements in each part is the same.

Such that : sum(B[1],..B[i]) = sum(B[i+1],...B[j]) = sum(B[j+1],...B[n])



Problem Constraints
1 <= A <= 105

-109 <= B[i] <= 109
'''


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        sum_list = sum(B)
        ways = 0
        if sum_list % 3 != 0:
            return ways
        prefix_sum = 0
        
        sum1 = int(sum_list/3)
        sum2 = 2*sum1
        
        third_cnt = 0

        for x in B[:-1]:
            prefix_sum += x
            
            if prefix_sum == sum2:
                ways += third_cnt
            
            if prefix_sum == sum1:
                third_cnt += 1

        return ways


if __name__ == '__main__':
    sol = Solution()
    B =  [0, 1, -1, 0]
    out = sol.solve(len(B), B)
    print(out)