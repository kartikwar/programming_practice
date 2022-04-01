'''
Problem Description
 
You are given a preorder traversal A, of a Binary Search Tree.

Find if it is a valid preorder traversal of a BST.


Input Format
First and only argument is an integer array A denoting the pre-order traversal.


Output Format
Return an integer:

0 : Impossible preorder traversal of a BST
1 : Possible preorder traversal of a BST


Example Input
Input 1:

A = [7, 7, 10, 10, 9, 5, 2, 8]

Example Output
Output 1:

0
'''


class Solution:
    # @param A : list of integers
    # @return an integer

    def solve(self, A):
        status = 1

        last_removed = 0

        stack = []

        for x in A:
            if last_removed > x:
                return 0
            while len(stack) !=0 and x > stack[-1]:
                last_removed = stack.pop()
            stack.append(x)
        
        return status

if __name__ == '__main__':
    sol = Solution()
    A = [7, 7, 10, 10, 9, 5, 2, 8]
    # A = [7, 5, 2, 10, 9, 7, 8, 10]
    # A = [10,5,12]
    # A=  [10,12,5]
    print(sol.solve(A))