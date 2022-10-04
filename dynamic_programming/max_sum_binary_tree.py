'''https://www.interviewbit.com/problems/max-sum-path-in-binary-tree/'''
import sys

# A node structure
class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.val = key
		self.left = None
		self.right = None

class Solution:
	def maxPathSum(self, root) :
		self.ans = -float('inf')

		def traverse_path(root):
			if not root:
				return 0
			left = max(traverse_path(root.left),0)
			right = max(traverse_path(root.right),0)
			val = root.val
			self.ans = max(self.ans,val+left+right)
			return val+max(left,right)
		
		traverse_path(root)
		return self.ans

if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	sol = Solution()
	print(sol.maxPathSum(root))