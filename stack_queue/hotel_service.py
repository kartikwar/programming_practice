'''https://www.interviewbit.com/problems/hotel-service/'''

class Solution:
	# @param A : list of list of integers
	# @param B : list of list of integers
	# @return a list of integers
	def nearestHotel(self, A, B):
		n = len(A)
		m = len(A[0])
		inf = 1 << 30
		dis = [[0 for i in range(1005)] for j in range(1005)]
		q = []
		
		# q will contain only hotels
		for i in range(n):
			for j in range(m):
				if (A[i][j] == 0):
					dis[i + 1][j + 1] = inf
				else:
					dis[i + 1][j + 1] = 0
					q.append([i + 1, j + 1])
		

		while (len(q)>0):
			curr = q[0]
			q.pop(0)
			x = curr[0]
			y = curr[1]
			if (dis[x][y + 1] == inf):
				dis[x][y + 1] = dis[x][y] + 1
				q.append([x, y + 1])
			
			if (dis[x][y - 1] == inf):
				dis[x][y - 1] = dis[x][y] + 1
				q.append([x, y - 1])
			
			if (dis[x + 1][y] == inf):
				dis[x + 1][y] = dis[x][y] + 1
				q.append([x + 1, y])
			
			if (dis[x - 1][y] == inf):
				dis[x - 1][y] = dis[x][y] + 1
				q.append([x - 1, y])
			
		
		ans = []
		for i in range(len(B)):
			ans.append(dis[B[i][0]][B[i][1]])
		
		return ans


if __name__ == '__main__':
	sol = Solution()
	A = [[0, 0],[1, 0]]
	B = [[1, 1],[2, 1],[1, 2]]
	print(sol.nearestHotel(A, B))