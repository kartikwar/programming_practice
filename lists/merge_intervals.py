# Definition for an interval.
class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution:
	# @param intervals, a list of Intervals
	# @param new_interval, a Interval
	# @return a list of Interval
	def insert(self, intervals, new_interval):
		output = []
		overlapping_intervals = []

		insert_point = -1
		
		input_0 = min(new_interval.start, new_interval.end)
		input_1 = max(new_interval.start, new_interval.end)
		
		# lower = None
		# upper = None
		
		# append_status = True
		# output.append(Interval(1,5))
		
		appending_indexs = []


		for index, inter in enumerate(intervals):	
			if not (max(input_0, inter.start) > min(input_1, inter.end)):
				overlapping_intervals.append(inter)
				appending_indexs.append(index)
			else:
				if max(input_0, input_1) < max(inter.start, inter.end):
					if insert_point == -1:
						insert_point = index
				output.append(inter)

		overlapping_starts = [a.start for a in overlapping_intervals]

		overlapping_ends = [a.end for a in overlapping_intervals]

		over_start = min(overlapping_starts + [input_0])

		over_end = max(overlapping_ends + [input_1])
			
		over_interval = Interval(over_start, over_end)

		if len(appending_indexs):
			insert_point = appending_indexs[0]
			output.insert(insert_point, over_interval)
		else:
			#find insert point
			if insert_point == -1:
				output.append(Interval(input_0, input_1))
			else:
				output.insert(insert_point, Interval(input_0, input_1))


		

		self.output	 = output	
		return output 
		
		
	def print_intervals(self, intervals):
		intervals = [[a.start, a.end] for a in intervals]
		print('out is          ', intervals)
		print("".join(['*']*100))
		# temp = expected_out
		# print('expected out is ', temp)
		temp = 0

if __name__ == "__main__":

	intervals =  [ (1, 2), (3, 6) ]

	new_interval = (8,10)


	intervals = [Interval(a[0], a[1]) for a in intervals]
	new_interval = Interval(new_interval[0], new_interval[1])

	sol = Solution()

	out = sol.insert(intervals, new_interval)

	sol.print_intervals(out)

	TEMP = 0