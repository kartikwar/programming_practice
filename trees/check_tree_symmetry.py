'''
Given a binary tree, check whether it is a mirror of itself (ie, 
symmetric around its center).


Problem Constraints
1 <= number of nodes <= 105



Input Format
First and only argument is the root node of the binary tree.



Output Format
Return 0 / 1 ( 0 for false, 1 for true ).



Example Input
Input 1:

	1
   / \
  2   2
 / \ / \
3  4 4  3
Input 2:

	1
   / \
  2   2
   \   \
   3    3


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 The above binary tree is symmetric. 
Explanation 2:

The above binary tree is not symmetric.


Solution Approach:
2 trees T1 and T2 are symmetric if
1) value of T1’s root is same as T2’s root
2) T1’s left and T2’s right are symmetric.
3) T2’s left and T1’s right are symmetric.

'''

from binarytree import build

def check_symmetry(T1, T2):
	symmetry = False
	
	if T1 is None and T2 is None:
		symmetry = True
		return symmetry

	if T1 is None and T2 is not None:
		return symmetry
	
	if T1 is not None and T2 is None:
		return symmetry

	if T1.val != T2.val:
		return symmetry
	
	left_symmetry = check_symmetry(T1.left, T2.right)
	right_symmetry = check_symmetry(T1.right, T2.left)
	symmetry = left_symmetry and right_symmetry

	return symmetry

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isSymmetric(self, A):
		out = check_symmetry(A.left, A.right)
		return int(out)

if __name__ == '__main__':
	a = [1,2,2,3,4,4,3]
	a = build(a)
	sol = Solution()
	out = sol.isSymmetric(a)
	print(out)





