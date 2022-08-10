#binary search leads to a faster search in a sorted list

def binary_search(a, value):
	status = False
	start = 0
	end = len(a) - 1
	
	while start <= end:
		middle = int((start + end) /2)
		if a[middle] < value:
			start = middle + 1
		elif a[middle] > value:
			end = middle -1
		else:
			status = True
			return middle
	
	# if a[start] == value:
	# 	status = True

	return -1

if __name__ == '__main__':
	status = binary_search([1,2,3,4,5], 8)
	temp = 0