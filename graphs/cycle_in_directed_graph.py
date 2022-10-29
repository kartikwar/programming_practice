'''https://www.interviewbit.com/problems/cycle-in-undirected-graph/'''
# from sklearn import neighbors
# import re

class Solution:

	def cycle_util(self, node, vis, g, call_stack):
		cycle_present = 0

		vis[node] = True

		call_stack[node] = True

		#recursively iterate all the nodes

		for i in g[node]:
			if vis[i] == False:
				if self.cycle_util(i, vis, g,call_stack):
					return 1
			elif call_stack[node] == True:
						cycle_present = 1
						return cycle_present
		
		call_stack[node] = False
		return cycle_present

	# @param A : integer
	# @param B : list of list of integers
	# @return an integer
	def solve(self, A, e):
		cycle_present = 0
		n=A
		g=[[] for i in range(n+1)]
		for i in e:
			g[i[0]].append(i[1])
			# g[i[1]].append(i[0])
		vis=[False]*(n+1)
		call_stack = [False]*(n+1)
		for curr in range(1,n+1):
			if vis[curr] == False:
				cycle_present = self.cycle_util(curr, vis, g, call_stack)

				if cycle_present:
					return 1

		return cycle_present


if __name__ == '__main__':
	sol = Solution()
	A = 3
	B = [  [1, 3], [2, 3] ,[3, 2]]
	print(sol.solve(A, B))