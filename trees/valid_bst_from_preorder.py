class Solution:
    # @param A : list of integers
    # @return an integer

    def solve(self, A):
        status = 1

        for ind, ele in enumerate(A):
            #find element greater then ele
            curr_ele = ele
            great_index = None
            for ind_nxt, ele in enumerate(A[ind+1:]):
                if ele > curr_ele:
                    if great_index is None:
                        great_index = ind_nxt

                if ele < curr_ele and great_index is not None:
                    #indx_nxt should be less then great_index
                    if ind_nxt > great_index:
                        status = 0

        return status

if __name__ == '__main__':
    sol = Solution()
    # A = [7, 7, 10, 10, 9, 5, 2, 8]
    # A = [7, 5, 2, 10, 9, 7, 8, 10]
    A = [10,5,12]
    # A=  [10,12,5]
    print(sol.solve(A))