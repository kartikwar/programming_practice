# Definition for an interval.
class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution:
	# @param intervals, a list of Intervals
	# @param new_interval, a Interval
	# @return a list of Interval
	def insert(self, intervals, newInterval):
		start = newInterval.start
		end = newInterval.end
		
		right = left = 0

		#right is current pointer

		# left is the pointer when newinterval is greater 

		while right < len(intervals):
			if start <= intervals[right].end:
				if end < intervals[right].start:
					break
				start = min(start, intervals[right].start)
				end = max(end, intervals[right].end)
			else:
				left += 1
			right += 1
		return intervals[:left] + [Interval(start, end)] + intervals[right:]
		
		
	def print_intervals(self, intervals):
		intervals = [[a.start, a.end] for a in intervals]
		print('out is          ', intervals)
		print("".join(['*']*100))
		# temp = expected_out
		# print('expected out is ', temp)
		temp = 0

if __name__ == "__main__":

	intervals =  [ (1, 3), (6, 9) ]

	new_interval = (2,5)


	intervals = [Interval(a[0], a[1]) for a in intervals]
	new_interval = Interval(new_interval[0], new_interval[1])

	sol = Solution()

	out = sol.insert(intervals, new_interval)

	sol.print_intervals(out)

	TEMP = 0