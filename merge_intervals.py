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
	# intervals = [ (6037774, 6198243), (6726550, 7004541), (8842554, 10866536), (11027721, 11341296), 
	# (11972532, 14746848), (16374805, 16706396), (17557262, 20518214), (22139780, 22379559), 
	# (27212352, 28404611), (28921768, 29621583), (29823256, 32060921), (33950165, 36418956), 
	# (37225039, 37785557), (40087908, 41184444), (41922814, 45297414), (48142402, 48244133), 
	# (48622983, 50443163), (50898369, 55612831), (57030757, 58120901), (59772759, 59943999), 
	# (61141939, 64859907), (65277782, 65296274), (67497842, 68386607), (70414085, 73339545), 
	# (73896106, 75605861), (79672668, 84539434), (84821550, 86558001), (91116470, 92198054), (96147808, 98979097) ]

	# intervals = [(1,2), (3,5), (6,7), (8,10), (12,16)]	
	
	# intervals = [(3,5), (6,7), (8,10), (12,16)]	

	# intervals = [(3,5), (6,7), (8,10), (12,16)]	

	# new_interval = (36210193, 61984219)

	# new_interval = (4,9)

	# new_interval = (1,2)

	# new_interval = (18,20)
	
	# expected_out = [(6037774, 6198243), (6726550, 7004541), (8842554, 10866536) ,(11027721, 11341296),  
	# (11972532, 14746848), (16374805, 16706396), (17557262, 20518214), (22139780, 22379559),
	# (27212352, 28404611), (28921768, 29621583), (29823256, 32060921), (33950165, 64859907),
	# (65277782, 65296274), (67497842, 68386607), (70414085, 73339545), (73896106, 75605861), 
	# (79672668, 84539434), (84821550, 86558001), (91116470, 92198054), (96147808, 98979097)] 

	intervals =  [ (1, 2), (3, 6) ]

	new_interval = (8,10)


	intervals = [Interval(a[0], a[1]) for a in intervals]
	new_interval = Interval(new_interval[0], new_interval[1])

	sol = Solution()

	out = sol.insert(intervals, new_interval)

	sol.print_intervals(out)

	TEMP = 0