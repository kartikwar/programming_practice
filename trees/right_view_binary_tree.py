'''
Given a binary tree A of integers. Return an array of integers 
representing the right view of the Binary tree.

Right view of a Binary Tree: is a set of nodes visible when 
the tree is visited from Right side.



Problem Constraints
1 <= Number of nodes in binary tree <= 105

0 <= node values <= 109 



Input Format
First and only argument is an pointer to the root of binary 
tree A.



Output Format
Return an integer array denoting the right view of the 
binary tree A.



Example Input
Input 1:

		1
	  /   \
	 2    3
	/ \  / \
   4   5 6  7
  /
 8 
Input 2:

	1
   /  \
  2    3
   \
	4
	 \
	  5


Example Output
Output 1:

 [1, 3, 7, 8]
Output 2:

 [1, 3, 4, 5]

 '''


def rightview(node, level, maxlevel, out):
	if node is None:
		return out, maxlevel
	if level >= maxlevel:
		maxlevel += 1
		out.append(node.val)
	out, maxlevel = rightview(node.right, level + 1, maxlevel, out)
	out, maxlevel = rightview(node.left, level + 1, maxlevel, out)
	return out, maxlevel

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def solve(self, A):
		out = []
		level = 0
		maxlevel = 0
		out, _ = rightview(A, level, maxlevel, out)
		return out