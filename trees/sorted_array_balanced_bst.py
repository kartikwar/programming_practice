'''
Given an array where elements are sorted in ascending order, 
convert it to a height balanced BST.

Balanced tree : a height-balanced binary tree is defined as 
a binary tree in which the depth of the two subtrees of 
every node never differ by more than 1.

Example :


Given A : [1, 2, 3]
A height balanced BST  : 

      2
    /   \
   1     3

Solution Hint:- What will happen when you choose middle element 
of array as root? Can you simulate the same thing for the left 
and right part of the array after that?

'''

from venv import create


class BinarySearchNode():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BalancedBST():
  def __init__(self, values):
    self.root = None
    self.values = values
    self.create_tree()
    
    
  def find_middle_element(self, values):
    lower = 0
    upper = len(values) - 1

    if (lower + upper ) % 2 == 0:
      middle = (lower + upper)//2
    else:
      middle = (lower + upper)//2 + 1

    return middle

  def insert_node(self, values):
    if len(values) == 0:
      return None
    middle_element = self.find_middle_element(values)
    left_array = values[:middle_element]
    right_array = values[middle_element+1:]
    root = BinarySearchNode(values[middle_element])
    root.left = self.insert_node(left_array)
    root.right = self.insert_node(right_array)
    return root

  def create_tree(self):
    self.root = self.insert_node(self.values)
    

if __name__ == '__main__':
    values = [1,2,3,4,5]
    tree = BalancedBST(values)
    temp = 0