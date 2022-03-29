'''
Given a BST node, return the node which has value just greater than the given node.

Example:

Given the tree

               100
              /   \
            98    102
           /  \
         96    99
          \
           97
Given 97, you should return the node corresponding to 98 as thats the value just greater than 97 in the tree.

If there are no successor in the tree ( the value is the largest in the tree, return NULL).

Using recursion is not allowed.

Assume that the value is always present in the tree.
'''

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        def find(val):
            node = A
            ans = None
            while node:
                if node.val > val:
                    node = node.left
                elif node.val < val:
                    node = node.right
                else:
                    return node
            
        def _findmin(node):
            while node.left:
                node = node.left
                
            return node
        
        rnode = find(B)
        if rnode.right:
            return _findmin(rnode.right)
        
        else:
            node = A
            successor = None
            while node != rnode:
                if node.val > rnode.val:
                    successor = node
                    node = node.left
                else:
                    node = node.right
            return successor 