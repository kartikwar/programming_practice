'''
Given a binary search tree, write a function to find the 
kth smallest element in the tree.
'''


from logging import root


class BinarySearchNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree():
    def __init__(self, values):
        self.root = None
        self.values = values
        self.create_tree()
        
    
    def insert_node(self, root, node):
        if root is None:
            root = node
        else:
            #check if node belongs at left
            if root.value > node.value:
                root.left = self.insert_node(root.left, node)
            else:
                root.right = self.insert_node(root.right, node)
        return  root
    
    

    def create_tree(self):
        for value in self.values:
            node = BinarySearchNode(value)
            #update tree
            self.root = self.insert_node(root=self.root, node=node)

    
    # left, root, right
    def in_order_traversal(self, root, values):
        if root is None:
            return 1, values
        else:
            self.in_order_traversal(root.left, values)
            # print(root.value)
            values.append(root.value)
            self.in_order_traversal(root.right, values)
        return 1, values
    


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        # A = tree.root
        _, values = tree.in_order_traversal(A, [])
        return values[B-1]


if __name__ == '__main__':
    A = [2,1,3]
    sol = Solution()
    tree = BinarySearchTree(A)
    print(sol.kthsmallest(tree.root, 2))