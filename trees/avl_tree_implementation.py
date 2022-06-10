'''
AVL trees are BSTs that balance automatically i.e.
the left subtree and the right subtree have a 
maximum height difference of 1.

Since these are balanced the search time complexity 
is O(logN), even in worst case scenarios.

Where as in normal BSTs, it can go upto O(N). Hence
AVL trees are very imp. data structures to store 
information.

This is the python implementation of AVL trees.
'''


class Node():
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        #parent of the current node
        self.parent = parent
        #stores the height of current node
        #root node has the highest height
        #and leaf node will have a height of 0
        self.height = 0


class AVLTree():
    def __init__(self):
        self.root = None
    
    def insert_node(self, node, data):
        if self.root is None:
            self.root = Node(data)
            return self.root

        if node is None:
            return Node(data)

        if node.data > data:
            node.left = self.insert_node(node.left, data)
            node.left.parent = node
        else:
            node.right = self.insert_node(node.right, data)
            node.right.parent = node

        left_height, right_height = 0, 0

        if node.left:
            left_height = node.left.height
        
        if node.right:
            right_height = node.right.height

        node.height = max(left_height, right_height) + 1

        return node

if __name__ == '__main__':
    values = [4,8,9,6,3,2]
    tree = AVLTree()
    for val in values:
        tree.insert_node(tree.root, val)
    # temp = 0