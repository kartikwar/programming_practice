'''
Given an array of all positive integers and an element “x”. 

You need to find out whether all array elements can be made equal or 
not by performing any of the 3 operations: add x to any element in 
array, subtract x from any element from array, do nothing.

This operation can be performed only once on an element of array.

Output Format
Return 1 if we can make all elements equal , otherwise return 0.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        global_set = set([])
        
        for ele in A:
            curr_set = []
            curr_set.append(ele)
            curr_set.append(ele-B)
            curr_set.append(ele+B)
            if len(global_set) ==0:
                global_set = curr_set
            else:
                for i, ele in enumerate(global_set):
                    if ele not in curr_set:
                        global_set[i] = None
            # print(curr_set)
            # print(global_set)
            

        curr_set = [ele for ele in global_set if ele is not None]
        # print(curr_set)
        return int(len(curr_set) > 0)


if __name__ == '__main__':
    A=[ 1, 2, 3, 1, 3, 1, 3, 3, 3, 2, 3, 1, 3, 1, 3, 3, 3, 3, 2, 3, 1, 2, 1, 3, 3, 3, 1, 2, 1, 1, 3, 1, 2, 3, 3, 2, 1 ]
    X=2
    sol = Solution()
    print(sol.solve(A, X))