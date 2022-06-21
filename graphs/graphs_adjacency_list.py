#in dfs all children are explored first
#i.e. like binary tree traversal

#in bfs all nodes at same level are explored first before 
#exploring the children 

class Node:
	def __init__(self, name):
		self.name = name
		self.adjacency_list = []
		self.visited = False

def depth_first_search(start_node):
	stack = [start_node]
	start_node.visited = True

	while stack:
		curr_node = stack.pop()
		curr_node.visited = True
		print(curr_node.name)
		for node in curr_node.adjacency_list:
			if not node.visited:
				node.visited = True
				stack.append(node)

def breadth_first_search(start_node):
	queue = [start_node]
	start_node.visited = True

	while queue:
		curr_node = queue.pop(0)
		print(curr_node.name)
		for node in curr_node.adjacency_list:
			if not node.visited:
				node.visited = True
				queue.append(node)

if __name__ == "__main__":
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	f = Node('f')

	a.adjacency_list = [b, c]
	b.adjacency_list = [a, d]
	c.adjacency_list = [a, d]
	d.adjacency_list = [e]
	e.adjacency_list = [a, f]

	breadth_first_search(a)
	depth_first_search(a)
	