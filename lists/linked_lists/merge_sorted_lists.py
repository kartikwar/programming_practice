'''
Merge two sorted linked lists and return it as a new list. 

The new list should be made by splicing together the nodes 
of the first two lists, and should also be sorted.

For example, given following linked lists :

  5 -> 8 -> 20 
  4 -> 11 -> 15
The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20
'''


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
		if A.val > B.val:
			main = B
			other = A
		else:
			main = A
			other = B 
		head = main
			
		while(other and main.next):
			if main.val < other.val:
				if main.next.val < other.val:
					main = main.next
				else:
					new_root = other.next
					nxt = main.next
					main.next = other
					other.next = nxt
					other = new_root
					main = main.next
		
		if main and other:
			if main.val < other.val:
				main.next = other


					
		return head

def create_list(values):
	prev_val = None
	for value in values:
		obj = ListNode(value)
		if prev_val is not None:
			prev_val.next = obj
		else:
			head = obj
		prev_val = obj
		
	return head

if __name__ == '__main__':
	A = create_list([5,8,20])
	B = create_list([4,11,15])
	sol = Solution()
	sol.mergeTwoLists(A, B)
