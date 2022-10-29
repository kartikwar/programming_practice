'''https://www.interviewbit.com/problems/cycle-in-undirected-graph/'''
# from sklearn import neighbors
# import re

class Solution:

	def cycle_util(self, node, vis, g, parent):
		cycle_present = 0

		vis[node] = True

		#recursively iterate all the nodes

		for i in g[node]:
			if vis[i] == False:
				if self.cycle_util(i, vis, g, node):
					return 1
			elif parent != i:
					cycle_present = 1
					return cycle_present

		return 0

	# @param A : integer
	# @param B : list of list of integers
	# @return an integer
	def solve(self, A, e):
		cycle_present = 0
		n=A
		g=[[] for i in range(n+1)]
		for i in e:
			g[i[0]].append(i[1])
			g[i[1]].append(i[0])
		vis=[False]*(n+1)
		for curr in range(1,n+1):
			if vis[curr] == False:
				cycle_present = self.cycle_util(curr, vis, g, -1)

				if cycle_present:
					return 1

		return cycle_present


if __name__ == '__main__':
	sol = Solution()

	A = 5
	B = [[1, 2], [1, 3], [2, 3], [1, 4], [4, 5]]
	print(sol.solve(A, B))