'''

You are given two numbers A and B.

You have to add them without using arithmetic 
operators and return their sum.



Problem Constraints
1 <= A, B <= 109


Input Format
The first argument is the integer A. The second 
argument is the integer B.


Output Format
Return a single integer denoting their sum.


Example Input
Input 1:
A = 3
B = 10
Input 2:

A = 6
B = 1


Example Output
Output 1:
13
Output 2:
7


Solution Approach:

If we denote the numbers in their binary 
form, we can use bitwise operators.

Note, that we can perform binary addition 
by keeping count of carry and sum.

Carry = A & B, Sum = A ^ B.

We can simply do this using recursion. 
Refer to the complete solution for 
more details.

'''


class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def addNumbers(self, A, B):
		while B:
			c = A & B
			A = A^B
			B = c << 1
		return A

if __name__ == '__main__':
	sol = Solution()
	out = sol.addNumbers(6,1)
	print(out)