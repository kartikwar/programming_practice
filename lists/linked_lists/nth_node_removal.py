'''
Problem link :- https://www.interviewbit.com/problems/remove-nth-node-from-list-end/
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
	def removeNthFromEnd(self, A, B):
		ptr1, index, ptr2 = A, 1, A
		
		# first initiliaze the ptrs
		while ptr2:
			ptr2 = ptr2.next
			index = index + 1
			if index == B + 1:
				break
		
		if not ptr2:
			#remove head node
			A = A.next
		else:
			#remove nth node
			prev = None
			while ptr2:
				prev = ptr1
				ptr2 = ptr2.next
				ptr1 = ptr1.next
			prev.next = ptr1.next
			
		return A

if __name__ == '__main__':
	A = [1, 2, 3, 4, 5]
	link_list = LinkedList(A)
	B = 2
	sol = Solution()
	out = sol.removeNthFromEnd(link_list.root, B)
	temp = 0