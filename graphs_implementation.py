from collections import deque

class GRAPH:

	def __init__(self,adjacency):
		if not adjacency:
			adjacency = {}
		self.adjacency = adjacency
	
	def insert(self,node):
		self.adjacency.update(node)
		pass
	
	def breadth_first_traversal(self, root):
		print('********************************')
		print('breadth first traversal')
		curr_nodes = [root]
		seen_nodes = []
		
		while len(curr_nodes) != 0:
			curr_node = curr_nodes.pop(0)
			
			if curr_node not in seen_nodes:
				print(curr_node)
				seen_nodes.append(curr_node)
				connected_nodes = adjacency[curr_node]
				curr_nodes = list(curr_nodes + list(connected_nodes))
	
	
	def depth_first_traversal(self, root):
		print('********************************')
		print('depth first traversal')
		curr_nodes = [root]
		seen_nodes = []
		
		while len(curr_nodes) != 0:
			curr_node = curr_nodes.pop()
			
			if curr_node not in seen_nodes:
				print(curr_node)
				seen_nodes.append(curr_node)
				connected_nodes = adjacency[curr_node]
				curr_nodes = list(curr_nodes + list(connected_nodes))


if __name__ == "__main__":
	adjacency = {
		'a' : set(['b', 'c']),
		'b' : set(['a', 'd']),
		'c' : set(['a', 'd']),
		'd' : set(['e']),
		'e' : set(['a', 'f'])
	}
	g = GRAPH(adjacency)
	g.insert({
		'f' : set(['d', 'c'])
	})
	g.breadth_first_traversal('a')
	g.depth_first_traversal('a')
	# temp = 0