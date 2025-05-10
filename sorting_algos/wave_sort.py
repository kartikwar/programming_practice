'''
Given an array of integers,  sort the array into a 
wave like array and return it, 

In other words, arrange the elements into a 
sequence such that  a1 >= a2 <= a3 >= a4 <= a5

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]

NOTE : If there are multiple answers possible, return the one 
thats lexicographically smallest. 

So, in example case, you will return [2, 1, 4, 3]
'''

class Solution:
	# @param A : list of integers
	# @return a list of integers
	def wave(self, A):
		A = sorted(A)
		curr = [float('-inf')]
		remaining = A

		operation_index = 0


		while len(remaining) != 0:
			curr.append(remaining.pop(0))
			if operation_index % 2 == 0:
				if curr[-1] < curr[-2]:
					#swap both
					curr[-1], curr[-2] = curr[-2], curr[-1]
			else:
				if curr[-1] > curr[-2]:
					#swap both
					curr[-1], curr[-2] = curr[-2], curr[-1]
			
			operation_index += 1 
			# pass
		curr.pop(0)
		return curr

if __name__ == '__main__':
	A = [ 5, 1, 3, 2, 4 ]
	sol = Solution()
	out = sol.wave(A)
	print(out)