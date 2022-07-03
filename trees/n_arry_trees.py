'''
NArryTree unlike binary trees, can have multiple children

it can be represnted in list with None separator.

For example:-
Input --- [1, None, 3,2,4,None, 5,6]

would convert into tree like this

                1
    

    3                   2               4


5       6

'''

class NArryNode():
    def __init__(self, value):
        self.value = value
        self.children = []
        
class NArryTree():
    def __init__(self, values):
        self.values = values
        self.root = None
        self.node_stack = []
        self.build_tree()

    def build_tree(self):
        parent_node = None

        for value in self.values:
            node = value
            if node is not None:
                node = NArryNode(value)

                self.node_stack.append(node)

                if parent_node is None:
                    pass
                else:
                    parent_node.children.append(node)

            else:
                # if parent_node is None:
                parent_node = self.node_stack.pop(0)

            if (self.root is None) and (parent_node is not None):
                self.root = parent_node

    #parent and then children
    # in binary tree, it is root, left, right
    def pre_order(self, output, node):
        if node is None:
            return output
        output.append(node.value)
        for child_node in node.children:
            self.pre_order(output, child_node)
        return output 
                
if __name__ == '__main__':
    tree = NArryTree([1, None, 3,2,4,None, 5,6])
    #root, left, right
    print(tree.pre_order([], tree.root))
    temp = 0