from binarytree import build

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isValidBST(self, A, val):
		is_valid = True
		if A is None:
			return int(is_valid)
		
		if A.left:
			if A.left.val < val:
				is_valid = self.isValidBST(A.left, A.val )
			else:
				is_valid = False
				return int(is_valid)
		
		if A.right:
			if A.right.val > val:
				is_valid = self.isValidBST(A.right, A.val)  
			else:
				is_valid = False
				return int(is_valid)
		
		return int(is_valid)


if __name__ == '__main__':
	a= [4, 2, 5, 1, 5, -1, -1, -1, -1, -1, -1]
	a = [ele if ele !=-1 else None for ele in a]
	# a = [None for ele in a if ele==-1]
	tree = build(a)
	sol = Solution()
	print(sol.isValidBST(tree, tree.val))
	temp = 0