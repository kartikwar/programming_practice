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
		
		input_0 = min(new_interval.start, new_interval.end)
		input_1 = max(new_interval.start, new_interval.end)
		
		lower = None
		upper = None
		
		append_status = True
		# output.append(Interval(1,5))
		
		for index in range(len(intervals)-1):
			
			inter = intervals[index]
			next_inter = intervals[index + 1]
			
			inter_start = inter.start
			inter_end = inter.end
			
			if (max(input_0, inter_start, inter_end) < next_inter.end)  \
			and append_status :
				lower = min(input_0, inter_start, inter_end)
				append_status = False
			
			if (max(input_1, inter_start, inter_end) < next_inter.end) \
			and not append_status:
				upper = max(input_1, inter_start, inter_end)
				append_status = True
				inter = Interval(lower, upper)
					
			
			if append_status:
				output.append(inter)
			
		output = output + [Interval(intervals[-1].start, intervals[-1].end)]
		
		if not lower:
			output = output + [Interval(input_0, input_1)]

		self.output	 = output	
		return output 
		
		
	def print_intervals(self, intervals):
		intervals = [[a.start, a.end] for a in intervals]
		print('out is          ', intervals)
		print("".join(['*']*100))
		temp = expected_out
		print('expected out is ', temp)
		temp = 0

if __name__ == "__main__":
	intervals = [ (6037774, 6198243), (6726550, 7004541), (8842554, 10866536), (11027721, 11341296), (11972532, 14746848), (16374805, 16706396), (17557262, 20518214), (22139780, 22379559), (27212352, 28404611), (28921768, 29621583), (29823256, 32060921), (33950165, 36418956), (37225039, 37785557), (40087908, 41184444), (41922814, 45297414), (48142402, 48244133), (48622983, 50443163), (50898369, 55612831), (57030757, 58120901), (59772759, 59943999), (61141939, 64859907), (65277782, 65296274), (67497842, 68386607), (70414085, 73339545), (73896106, 75605861), (79672668, 84539434), (84821550, 86558001), (91116470, 92198054), (96147808, 98979097) ]
	new_interval = (36210193, 61984219)
	expected_out = [(6037774, 6198243), (6726550, 7004541), (8842554, 10866536) ,(11027721, 11341296),  
	(11972532, 14746848), (16374805, 16706396), (17557262, 20518214), (22139780, 22379559),
	(27212352, 28404611), (28921768, 29621583), (29823256, 32060921), (33950165, 64859907),
	(65277782, 65296274), (67497842, 68386607), (70414085, 73339545), (73896106, 75605861), 
	(79672668, 84539434), (84821550, 86558001), (91116470, 92198054), (96147808, 98979097)] 


	intervals = [Interval(a[0], a[1]) for a in intervals]
	new_interval = Interval(new_interval[0], new_interval[1])

	sol = Solution()

	out = sol.insert(intervals, new_interval)

	sol.print_intervals(out)

	TEMP = 0