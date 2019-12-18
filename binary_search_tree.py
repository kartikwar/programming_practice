class TreeNode:

	def __init__(self,key):
		self.data = key
		self.left = None
		self.right = None

	def insert_node(self, root):
		if root == None:
			root.data = self.data
			root.left = self.left
			root.right = self.right
		else:
			if root.data > self.data:
				#insert left
				if root.left == None:
					# self.insert_node(root.left, node)
					root.left = self
					# root.left.left = self.left
					# root.left.right = self.right
				else:
					self.insert_node(root.left)
			else:
				#insert right
				if root.right == None:
					# self.insert_node(root.left, node)
					root.right = self
					# root.right.left = self.left
					# root.right.right = self.right
				else:
					self.insert_node(root.right) 
		# pass

	# left, root, right
	def in_order_traversal(self, root):
		if root: 
			self.in_order_traversal(root.left) 
			print(root.data) 
			self.in_order_traversal(root.right) 
		# pass
	
	# root, left, right
	def pre_order_traversal(self, root):
		pass
	
	# left, right, root
	def post_order_traversal(self, root):
		pass

if __name__ == "__main__":
	r = TreeNode(55)
	a = TreeNode(35).insert_node(r)
	b = TreeNode(25).insert_node(r)
	b = TreeNode(45).insert_node(r)
	b = TreeNode(75).insert_node(r)
	b = TreeNode(65).insert_node(r)
	b = TreeNode(85).insert_node(r)
	r.in_order_traversal(r)
	# insertNode(r,TreeNode(45)) 
	# insertNode(r,TreeNode(75)) 
	# insertNode(r,TreeNode(65)) 
	# insertNode(r,TreeNode(85)) 
	# b
	# TreeNode.insert_node
	pass