'''https://www.interviewbit.com/problems/flatten-binary-tree-to-linked-list/'''


class BinarySearchNode():
    def __init__(self, value):
        self.val = value
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
            if root.val > node.val:
                root.left = self.insert_node(root.left, node)
            else:
                root.right = self.insert_node(root.right, node)
        return  root
    
    def create_tree(self):
        for value in self.values:
            node = BinarySearchNode(value)
            #update tree
            self.root = self.insert_node(root=self.root, node=node)

    def flatten_helper(self, node, prev):
        if node is None:
            return
        
        if node.right:
            prev = self.flatten_helper(node.right, prev) 
            
        if node.left:
            prev = self.flatten_helper(node.left, prev)
        
        node.left = None
        node.right = prev
        
        prev = node

        return prev

    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        prev = None
        self.flatten_helper(A, prev)
        return A

if __name__ == '__main__':
    a = [4, 5, 6, 2, 1, 3]
    tree = BinarySearchTree(a)
    tree.flatten(tree.root)
    temp = 0
