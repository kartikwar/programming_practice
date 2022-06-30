'''
Dijsktras algorithm is used to find the shortest path from 
start node to end node. 

It is a greedy algorithm that tries to find the shortest route 
for each given node in a graph.

Since its greedy, it decides which node to visit next, 
based on which node is currently at minium distance from 
the start node

Its also dynamic in nature i.e the distances are updated dynamically, 
since you might find a path for any given node which is shorter than 
earlier shortest path.

This is a adjacency matrix represnentation of this algo. In adjacency 
list representation heap is used which makes the implementation faster
than this one.

For visualization see the figure dijsktras_algo.png
'''

import sys

class Node:
    def __init__(self, name, index, adjancy_matrix):
        self.name = name
        self.visited = False
        self.index = index
        self.shortest_path = []

class DijsktrasAlgo:
    def __init__(self, adjancy_matrix):
        self.adjancy_matrix = adjancy_matrix
        self.nodes = self.initialize_nodes()
        self.distances = [sys.maxsize for i in range(len(adjancy_matrix))]
        self.distances[0] = 0
        self.calculate()
    
    def initialize_nodes(self):
        nodes = []
        for i in range(len(self.adjancy_matrix)):
            name = chr(i % 26 + 65)  
            node = Node(name, i, self.adjancy_matrix)
            # if i ==0 :
            #     node.shortest_path = ['A']
            nodes.append(node)
        return nodes

    def get_connected_nodes(self, node):
        node_index = node.index
        weights = self.adjancy_matrix[node_index]
        nodes = [
            (self.nodes[i], self.distances[i]) for i in range(len(self.distances)) if self.nodes[i].visited == False 
            and self.distances[i] != 0 and i !=node_index
        ]
        return nodes

    def get_closest_node(self, curr_node):
        min_distance = sys.maxsize
        closest = None
        for i in range(len(self.distances)):
            if i != 0 and i!= curr_node.index and self.nodes[i].visited == False: 
                if self.distances[i] < min_distance:
                    min_distance = self.distances[i]
                    closest = self.nodes[i]
        return closest

    def assign_distances(self, curr_node):
        node_index = curr_node.index
        curr_distance = self.distances[node_index]
        weights = self.adjancy_matrix[node_index]
        for i in range(len(self.distances)):
            if weights[i] != 0:
                if curr_distance + weights[i] < self.distances[i]:
                    self.distances[i] = curr_distance + weights[i]
                    self.nodes[i].shortest_path = curr_node.shortest_path +  [curr_node.name]

    def calculate(self):
        node_index = 0
        
        curr_node = self.nodes[node_index]
        
        while(curr_node):
            print('currently exploring node ' , curr_node.name)
            self.assign_distances(curr_node)
            nearest_node = self.get_closest_node(curr_node)
            curr_node.visited = True
            curr_node = nearest_node


                




if __name__ == '__main__':
    adjancy_matrix = [[0, 7, 5, 2, 0, 0],
                       [7 , 0, 0, 0, 3, 0],
                       [5, 0, 0, 10, 4, 0],
                       [2, 0, 10, 0, 0, 2],
                       [0, 3, 4, 0, 0, 6], 
                       [0, 0, 0, 2, 6, 0]]

    # adjancy_matrix = [
    #     [0, 5, 0, 0, 9, 0, 0, 8],
    #     [0, 0, 12, 15, 0, 0, 0, 0],
    #     [0, 0, 0, 3, 0, 0, 11, 0],
    #     [0, 0, 0, 0, 0, 0, 9, 0],
    #     [0, 0, 0, 0, 0, 4, 20, 5],
    #     [0, 0, 1, 0, 0, 0, 13, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 7, 0, 0, 6, 0, 0],
    # ]

    # import numpy as np
    # print(np.shape(np.array(adjancy_matrix)))

    da = DijsktrasAlgo(adjancy_matrix)
    print(da.distances)
    # print(da.nodes[-1].shortest_path)

    for node in da.nodes:
        print('for node ', node.name)
        print('shortest distance is ')
        print(node.shortest_path)