'''https://www.interviewbit.com/problems/anti-diagonals'''


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def diagonal(self, A):
		out = []
		N = len(A)
		# i,j = 0 , 0

		visited = [[0 for i in range(len(A))] for j in range(len(A))]

		for row in range(N):
			for col in range(N):
				res = []
				i = row
				j = col

				if visited[i][j]:
					continue 

				while i> -1 and i < N and j > -1 and j < N:
					visited[i][j] = 1
					res.append(A[i][j])
					i += 1
					j -= 1
				
				out.append(res)

		return out

			 


if __name__ == '__main__':
	sol = Solution()
	A =  [[1, 2, 3], [4, 5, 6], [7,8,9]] 
	print(sol.diagonal(A))
