'''https://www.interviewbit.com/problems/clone-graph'''

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        from collections import deque
        q = deque()
        family = {}
        q.append(node)
        root = UndirectedGraphNode(node.label)
        family[node] = root
        while(len(q) > 0):
            node = q[0]
            q.popleft()
            for i in node.neighbors:
                if i not in family:
                    # if not present in family, create a child
                    copy = UndirectedGraphNode(i.label)
                    family[i] = copy
                    q.append(i)
                family[node].neighbors.append(family[i])
                    
        return root



if __name__ == '__main__':
    fourth = UndirectedGraphNode(4)
    fourth.neighbors.append(UndirectedGraphNode(5))
    fourth.neighbors.append(UndirectedGraphNode(6))

    three = UndirectedGraphNode(3)
    two = UndirectedGraphNode(2)

    one = UndirectedGraphNode(1)
    one.neighbors.append(two)
    one.neighbors.append(three)
    one.neighbors.append(fourth)

    sol = Solution()
    sol.cloneGraph(one)