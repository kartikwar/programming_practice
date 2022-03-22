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
	
	

	
	def interchange_values(self, a , b):
		temp = a
		a = b
		b = temp
		return a, b
	
	def flip_tree(self, root):
		if root is None:
			return None
		else:
			root.left, root.right = self.interchange_values(root.left, root.right)
			self.flip_tree(root.left)
			self.flip_tree(root.right)
			# else:
			# 	root.right = self.insert_node(root.right, node)
		return  root



	def create_tree(self):
		for value in self.values:
			node = BinarySearchNode(value)
			#update tree
			self.root = self.insert_node(root=self.root, node=node)
			
	def search_tree(self, root, value):
		status = False
		
		if root is None:
			return status
		
		if root.value == value:
			status = True
		
		else:
			if root.value > value:
				status = self.search_tree(root.left, value)
			else:
				status = self.search_tree(root.right, value)
		
		return status
	
	# left, root, right
	def in_order_traversal(self, root):
		if root is None:
			return 1
		else:
			self.in_order_traversal(root.left)
			print(root.value)
			self.in_order_traversal(root.right)
		return 1
	
	# root, left, right
	def pre_order_traversal(self, root):
		if root is None:
			return 1
		else:
			# self.pre_order_traversal(root)
			print(root.value)
			self.pre_order_traversal(root.left)
			self.pre_order_traversal(root.right)
		return 1
	
	# left, right, root
	def post_order_traversal(self, root):
		if root is None:
			return 1
		else:
			self.in_order_traversal(root.left)
			self.in_order_traversal(root.right)
			print(root.value)
			return 1
		pass
	
	def check_if_tree_is_bst(self, root, status):
		
		if root is None:
			return status
		else:
			status_right = True
			status_left= True
			
			if root.left and root.right:
			
				if root.value > root.left.value and root.value < root.right.value:
					# status = True
					status_left = self.check_if_tree_is_bst(root.left, status= True)
					status_right = self.check_if_tree_is_bst(root.right, status=True)
					return status_left and status_right
			
				else:
					return False
			
			elif root.left:
				
				if root.value > root.left.value:
					# status = True
					status_left = self.check_if_tree_is_bst(root.left, status=True)
					status_right = self.check_if_tree_is_bst(root.right, status=True)
					return status_left and status_right
				
				else:
					return False
			
			elif root.right:
				if root.value < root.right.value:
					# status = True
					status_left = self.check_if_tree_is_bst(root.left, status=True)
					status_right = self.check_if_tree_is_bst(root.right, status=True)
					return status_left and status_right
				
				else:
					return False
		
			else:
				return status

if __name__ == "__main__":
	values = [8, 3, 10, 14, 1,6, 4, 7, 13]
	tree = BinarySearchTree(values)
	found = tree.search_tree(root=tree.root, value=38)
	tree.post_order_traversal(root=tree.root)
	flipped_tree = tree.flip_tree(root = tree.root)
	tree_is_bst = tree.check_if_tree_is_bst(root= flipped_tree, status=True)
	root = tree.root
	
