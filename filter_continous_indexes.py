def filter_indexes(ideal_indexes):
	filtered_indexes = []
	start = None
	end = None

	for i, ele in enumerate(ideal_indexes[:-1]):
		
		if start == None:
			start = ele
		
		if end  == None:
			end = ele

		curr = i
		nxt = i + 1

		if ideal_indexes[curr] + 1 == ideal_indexes[nxt]:
			end = ideal_indexes[nxt]

		else:
			if start != end:
				filtered_indexes.append([start,end])
			start = None
			end = None
			
	if start != None  and end != None:
		# if start != end:
		filtered_indexes.append([start, end])

	return filtered_indexes




if __name__ == "__main__":
	ideal_indexes = [0, 1, 2, 3, 4]
	indexes = filter_indexes(ideal_indexes)
	temp = 0