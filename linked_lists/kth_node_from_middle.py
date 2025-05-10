'''
Problem link :- https://www.interviewbit.com/problems/kth-node-from-middle/
'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class LinkedList:
	def __init__(self, A):
		self.values = A
		self.root = None
		self.build_list()

	def build_list(self):
		for val in self.values:
			node = ListNode(val)
			if self.root is None:
				self.root = node
				curr_node = self.root
			else:
				curr_node.next = node
				curr_node = curr_node.next

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def solve(self, A, B):
		ptr1, index, ptr2, head, N = A, 1, A, A, 0
		
		while head:
			head = head.next
			N += 1    
		
		middle = N//2 + 1
		
		# first initiliaze the ptrs
		while ptr2:
			ptr2 = ptr2.next
			index = index + 1
			if index == B + 1:
				break
		
		if not ptr2:
			A = -1
		else:
			while ptr2:
				if index == middle:
					break
				ptr2 = ptr2.next
				ptr1 = ptr1.next
				index += 1
			if ptr2:
				A = ptr1.val
			else:
				A = -1

		return A

if __name__ == '__main__':
	A = [ 725, 479, 359, 963, 465, 706, 146, 282, 828, 962 ]
	link_list = LinkedList(A)
	B = 2
	sol = Solution()
	out = sol.solve(link_list.root, B)
	temp = 0