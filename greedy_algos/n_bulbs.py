'''Problem Link:- https://www.interviewbit.com/problems/interview-questions/'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):
		switch_count = 0
		
		for bulb in A:
			if switch_count%2 !=0:
				bulb = 1 - bulb
			
			if bulb==0:
				switch_count += 1

		return switch_count