'''

Given a sorted linked list, delete all duplicates such 
that each element appear only once.

For example,

Given 1->1->2, return 1->2.

Given 1->1->2->3->3, return 1->2->3.

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
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
		a = set([])
		curr_node = A
		prev_node = A
		while curr_node is not None:
			val = curr_node.val
			if val in a:
				prev_node.next = curr_node.next
			else:
				# if prev_node != curr_node:
				# 	prev_node.next = curr_node
				prev_node = curr_node 
				a.add(val)
			# prev_node = curr_node
			curr_node = curr_node.next

		return A


if __name__ == '__main__':
	A = [1,1,1,1,1,2,3,3]
	link_list = LinkedList(A)
	sol = Solution()
	out = sol.deleteDuplicates(link_list.root)
	temp = 0