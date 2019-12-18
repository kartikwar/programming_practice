from collections import deque

class GRAPH:

	def __init__(self,adjacency):
		if not adjacency:
			adjacency = {}
		self.adjacency = adjacency
	
	def breadth_first_traversal(self, startnode):
		print('********************************')
		print('breadth first traversal')
		queue = deque([startnode])

		seen_nodes = set([])

		while queue:
			curr_node = queue.popleft()

			if curr_node not in seen_nodes:
			
				seen_nodes.add(curr_node)
				print('node is ', curr_node)

				for node in self.adjacency[curr_node]:
					queue.append(node)
	
	def depth_first_traversal(self, startnode):
		print('********************************')
		print('depth first traversal')
		queue = deque([startnode])

		seen_nodes = set([])

		while queue:
			curr_node = queue.pop()

			if curr_node not in seen_nodes:
			
				seen_nodes.add(curr_node)
				print('node is ', curr_node)

				for node in self.adjacency[curr_node]:
					queue.append(node)

	def insert(self,node):
		self.adjacency.update(node)
		pass		

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