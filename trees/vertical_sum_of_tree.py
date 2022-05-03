'''
You are given the root of a binary tree A.

You have to find the vertical sum of the tree.

A vertical sum denotes an array of sum of the different verticals of a binary tree,

where the leftmost vertical sum is the first element of the array and rightmost vertical is the last.



Problem Constraints
1 <= Number of nodes in the binary tree <= 105
1 <= Ai <= 103


Input Format
The first argument is the root of a binary tree A.


Output Format
Return an array denoting the vertical sum of the binary tree.


Example Input
Input 1:
A =     1
      /   \
     2     3
    / \   / \
   4   5 6   7
Input 2:

A =     1
       /
      2
     /
    3


Example Output
Output 1:
[4, 2, 12, 3, 7]
Output 2:

[3, 2, 1]


Solution Approach:
We need to check the Horizontal Distances from the root 
for all nodes. 

If two nodes have the same Horizontal Distance (HD), then 
they are on the same vertical line.  

HD for root is 0, a right edge (edge connecting to 
right subtree) is considered as +1 horizontal 
distance and a left edge is considered as -1 
horizontal distance.

So, we just need to have a map, where we add elements 
to the HD value, then return the array in the end.
'''


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


def compute_distance(node, distance, is_left, distance_map):
    
    if node is None:
        return distance_map
    

    if is_left is None:
        print('root node')
    # distance = distance_map[node.val]
    elif is_left:
        distance -= 1
    # elif is_left is None:
    #     distance = distance
    else:
        distance += 1

    if distance in distance_map:
        distance_map[distance] = distance_map[distance] + node.val
    else:
        distance_map[distance] = node.val

    distance_map = compute_distance(node.left, distance, True, distance_map)
    distance_map = compute_distance(node.right, distance, False, distance_map)


    return distance_map

if __name__ == '__main__':
    a = [4,2,6,1,3,5,7]
    a = BinarySearchTree(a)
    distance_map = compute_distance(a.root, 0, None, {})
    sorted_keys = sorted([key for key in distance_map.keys()])
    out = [distance_map[key] for key in sorted_keys]
    temp = 0
