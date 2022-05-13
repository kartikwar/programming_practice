'''
Problem Description
 
 

Given the start day of the month A and 
number of days in the month B, find 
number of sundays in the month.


Problem Constraints
A = {"Monday", "Tuesday", "Wednesday", "Thursday", 
"Friday", "Saturday", "Sunday"}
1 <= B <= 109


Input Format
First argument is an string A.
Second argument is an integer B.


Output Format
Return an integer.


Example Input

Input 1:
A = "Sunday"
B = 1

Input 2:
A = "Monday"
B = 14


Example Output
Output 1: 1
Output 2: 2


Example Explanation

Explanation 1:The only day in the 
month is sunday.

Explanation 2: The 7th and 14th day 
of the month will be sunday

'''


class Solution:
	# @param A : string
	# @param B : integer
	# @return an integer
	def solve(self, A, B):
		number_of_days = 0
		days = {"Monday" : 1, "Tuesday" : 2, "Wednesday" : 3, 
			"Thursday" : 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
		first_day = days[A]
		first_sunday = 8 - first_day
		if first_sunday > B:
			return 0
		else:
			number_of_days += 1
		remaining_days = B - first_sunday
		
		return number_of_days + remaining_days//7

if __name__ == '__main__':
	sol = Solution()
	sol.solve("Thursday", 10)
	pass