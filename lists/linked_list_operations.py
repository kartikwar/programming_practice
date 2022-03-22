class LinkedList():
	def __init__(self, value):
		self.value = value
		self.next = None
	

def create_list(values):
	prev_val = None
	for value in values:
		obj = LinkedList(value)
		if prev_val is not None:
			prev_val.next = obj
		else:
			head = obj
		prev_val = obj
		
		
	return head
	pass


def create_cyclic_list(values, cycle_at):
	all_objects = []
	prev_val = None
	last_index = len(values) -1
	
	for index, value in  enumerate(values):
		obj = LinkedList(value)
		if prev_val is not None:
			prev_val.next = obj
		else:
			head = obj
		prev_val = obj
		
		all_objects.append(obj)
		
		if index == last_index:
			obj.next = all_objects[cycle_at]
	
	return head


def reverse_list(root):
	nxt, prev, curr = None, None, None
	curr = root
	while curr is not None:
		nxt = curr.next
		curr.next = prev
		prev = curr
		curr = nxt
	return prev


def detect_cycle(root):
	curr = root
	seen_nodes = []
	status = False
	while curr is not None:
		if curr not in seen_nodes:
			seen_nodes.append(curr)
		else:
			status = True
			break
		curr = curr.next
	return status

"""
given a linked list, find the nth node from end
"""
def detect_nth_from_end(root, n):
	pointer1 = root
	pointer2 = root
	
	pointer2_move_status = False
	
	nodes_moved = 0
	
	while pointer1 != None:
		
		pointer1 = pointer1.next
		nodes_moved += 1

		if pointer2_move_status:
			pointer2 = pointer2.next
		
		if nodes_moved == n:
			pointer2_move_status = True
			#start moving pointer 2
		
	
	return pointer2



if __name__ == "__main__":
	
	root_no_cycle = create_list([1,2, 3,4 , 5, 6, 7, 8])
	
	root_cycle = create_cyclic_list([1,2,3, 4, 5] , cycle_at= 2)
	
	root_no_cycle = reverse_list(root_no_cycle)
	
	status = detect_cycle(root_no_cycle)
	
	nth_node = detect_nth_from_end(root_no_cycle, 5)
	
	temp = 0