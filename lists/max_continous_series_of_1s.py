"""
You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
Find the position of zeros which when flipped will produce maximum continuous series of 1s.

Input :
Array = {1 1 0 1 1 0 0 1 1 1 }
M = 1

Output :
[0, 1, 2, 3, 4]
"""



class Solution:


	def maxone(self, A, B):
		max_length = 0
		remaining_width = B + 1
		curr_length = 0
		index = 0
		zeros = []
		lowest, highest, max_high, max_low = 0, 0, 0, 0
		
		while index < len(A):
			val = A[index]
			
			if val != 0:
				curr_length += 1
				highest += 1

			else:
				zeros.append(index)
				
				remaining_width -= 1

				if remaining_width != 0:
					curr_length +=1
					highest += 1

				else:
					lowest = zeros.pop(0) + 1
					highest = highest + 1
					remaining_width = 1
			
			if highest - lowest > max_length:
				max_length = curr_length
				max_high = highest
				max_low = lowest
			
			index += 1
		
		return list(range(max_low, max_high))
		
if __name__ == '__main__':
	# A = [1, 1, 0, 1, 1, 0 ,0 ,1 ,1 ,1 ]
	A = [ 1, 0, 1, 0, 1, 1, 1, 1, 0, 0,  0,  0,  1,  1,  1,  1,  0 ]
	d = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ]
	M = 4
	
	sol = Solution()
	out = sol.maxone(A=A, B=M)
	temp = 0