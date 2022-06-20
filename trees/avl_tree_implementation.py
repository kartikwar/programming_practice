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

Left vs right rotations


		A							B

	B		E					C		A

C		D							D		E		

			right rotation ---------> 
			left rotation <---------

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

	"""function to print tree"""
	def __repr__(self):
		if self.root==None: return ''
		content='\n' # to hold final string
		cur_nodes=[self.root] # all nodes at current level
		cur_height=self.root.height # height of nodes at current level
		sep=' '*(2**(cur_height-1)) # variable sized separator between elements
		while True:
			cur_height+=-1 # decrement current height
			if len(cur_nodes)==0: break
			cur_row=' '
			next_row=''
			next_nodes=[]

			if all(n is None for n in cur_nodes):
				break

			for n in cur_nodes:

				if n==None:
					cur_row+='   '+sep
					next_row+='   '+sep
					next_nodes.extend([None,None])
					continue

				if n.data!=None:       
					buf=' '*int((5-len(str(n.data)))/2)
					cur_row+='%s%s%s'%(buf,str(n.data),buf)+sep
				else:
					cur_row+=' '*5+sep

				if n.left!=None:  
					next_nodes.append(n.left)
					next_row+=' /'+sep
				else:
					next_row+='  '+sep
					next_nodes.append(None)

				if n.right!=None: 
					next_nodes.append(n.right)
					next_row+='\ '+sep
				else:
					next_row+='  '+sep
					next_nodes.append(None)

			content+=(cur_height*'   '+cur_row+'\n'+cur_height*'   '+next_row+'\n')
			cur_nodes=next_nodes
			sep=' '*int(len(sep)/2) # cut separator size in half
		return content
	
	def pos_of_node(self, node):
		is_left = False
		if node.parent.left:
			if node.parent.left.data == node.data:
				#current node is left node
				is_left = True
		return is_left

	def min_val_subtree(self, node):
		'''
		find the min val in a subtree
		'''
		if node is None:
			return
		if node.left:
			return self.min_val_subtree(node.left)
		else:
			return node

	def get_height(self, node):
		if node is None:
			return -1
		else:
			return node.height

	def calculate_balance(self, node):
		'''a node is imbalanced and requires rotations
		if the balance factor is either greater than 
		1 or less than -1'''
		if node is None:
			return 0
		else:
			return self.get_height(node.left) - self.get_height(node.right)	


	"""perform left rotation"""
	def rotate_left(self, node):
		print("Rotating to the left on node", node.data)
		print('left rotate coming soon')

	"""perform right rotation"""
	def rotate_right(self, node):
		print("Rotating to the right on node", node.data)
		temp_left_node = node.left
		t = temp_left_node.right
		temp_left_node.right = node
		node.left = t
		if t is not None:
			t.parent = node
		temp_parent = node.parent
		node.parent = temp_left_node
		temp_left_node.parent = temp_parent

		if temp_left_node.parent is not None and temp_left_node.parent.left == node:
			temp_left_node.parent.left = temp_left_node

		if temp_left_node.parent is not None and temp_left_node.parent.right == node:
			temp_left_node.parent.right = temp_left_node

		if node == self.root:
			self.root = temp_left_node

		node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
		temp_left_node.height = max(self.get_height(temp_left_node.left), self.get_height(temp_left_node.right))


	'''fix the violation of balance'''
	def violation_helper(self, node):
		balance = self.calculate_balance(node)
		#left heavy
		if balance > 1:
			if self.calculate_balance(node.left) < 0:
				#left right case
				self.rotate_left(node.left)
				temp = 0
			self.rotate_right(node)

		#right heavy:
		if balance < -1:
			if self.calculate_balance(node.right) > 0:
				#right left case
				self.rotate_right(node.right)
			self.rotate_left(node)
			temp = 0


	'''check violation at parent node 
	and if it exists, handle it'''
	def handle_violation(self, node):
		while node:
			left_height = self.get_height(node.left)
			right_height = self.get_height(node.right)
			node.height = max(left_height, right_height) + 1
			balance = self.calculate_balance(node)
			if  balance > 1 or balance < -1:
				print('balance violated at ', node.data)
				temp = 0
			self.violation_helper(node)
			node = node.parent
			# self.handle_violation(node)
		# else:
		# 	print('node is None')

	def remove_node(self, node, data):
		if self.root is None:
			return

		if node is None:
			return

		if node.data == data:
			#node for deletion found
			
			if node.data == self.root.data:
				#node is root node
				self.root = None

			elif not (node.left or node.right):
				#node is leaf node
				is_left = self.pos_of_node(node)
				if is_left:
					node.parent.left = None
				else:
					node.parent.right = None

			elif (node.left is None) != (node.right is None):
				#atleast one node is None
				#find the position of node i.e. left vs right
				is_left = self.pos_of_node(node)

				if is_left:
					if node.left:
						node.parent.left = node.left
					else:
						node.parent.left = node.right
				else:
					if node.left:
						node.parent.right = node.left
					else:
						node.parent.right = node.right

			else:
				#node has two children
				#first find the smallest element in right most tree
				min_node = self.min_val_subtree(node.right)
				#switch the curr node with that element
				min_node.data, node.data = node.data, min_node.data
				#recursively perform the same operation
				self.remove_node(node.right, data)

		elif node.data > data:
			self.remove_node(node.left, data)
			# node.left.parent = node
		else:
			self.remove_node(node.right, data)
			# node.right.parent = node

		return

	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			self.insert_node(data, self.root)
		

	
	def insert_node(self, data, node):
		if data < node.data:
			if node.left:
				self.insert_node(data, node.left)
			else:
				node.left = Node(data, node)
				node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

		else:
			if node.right:
				self.insert_node(data, node.right)
			else:
				node.right = Node(data, node)
				node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1	

		self.handle_violation(node)


if __name__ == '__main__':
	# values = [4,3,8,2, 6,9,5]
	values = [32,10,55,1,19,41,16,12]
	tree = AVLTree()
	for val in values:
		tree.insert(val)
	# print(tree)
	# tree.remove_node(tree.root, 8)
	print(tree)
	# print(tree.calculate_balance(tree.root.left))
	