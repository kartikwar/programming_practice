'''
kth smallest element is the minimum possible n such that there are at least k elements in the array <= n.
In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while the arrays are 0 based )
'''

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        heap=list(A)
        heap = sorted(heap)
        return heap[B-1]


if __name__ == "__main__":
	A = [2, 1, 4, 3, 3]
	B = 3

	sol = Solution()
	out = sol.solve(A=A, B=B)
	pass