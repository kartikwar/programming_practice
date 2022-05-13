'''
Given an integer A, return the number 
of trailing zeroes in A!.

Note: Your solution should be in logarithmic 
time complexity.


Problem Constraints
0 <= A <= 10000000

Input Format
	First and only argumment is 
	integer A.

Output Format
	Return an integer, the answer to 
	the problem.

Example Input
Input 1: A = 4
Input 2: A = 5

Example Output
Output 1: 0

Output 2: 1

Solution Approach :- Refer the article 
for detailed explanation - 
https://www.interviewbit.com/blog/trailing-zeroes-in-factorial/

'''

class Solution:
	# @param A : integer
	# @return an integer
	def trailingZeroes(self, A):
		b = None
		number_of_zeros = 0
		power = 1
		while b != 0:
			b = A//(5**power)
			# if b >0:
			number_of_zeros += b
			power += 1
		return number_of_zeros