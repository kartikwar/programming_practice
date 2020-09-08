"""
Given an array of objects (each has some height and width),
also given a sheet of dimensions of some height nad width.
Its required to print these objects on these sheets. Find out how many
sheets will be required to print these
"""

class Solution:
	
	def __init__(self):
		pass


	def solve(self, objects, sheet_dimensions):
		rem_hei = sheet_dimensions[0]
		rem_wid = sheet_dimensions[1]
		number_of_sheets = 0
		
		if len(objects):
			number_of_sheets = 1
		
		for object in objects:
			object_height = object[0]
			object_wid = object[1]
			
			if object_height > sheet_dimensions[0] or object_wid > sheet_dimensions[1]:
				print('invalid dimensions')
				continue
			
			if rem_hei < object_height or rem_wid < object_wid:
				number_of_sheets += 1
				rem_hei = sheet_dimensions[0] - object_height
				rem_wid = sheet_dimensions[1] - object_wid
			
			else:
				rem_hei = rem_hei - object_height
				rem_wid = rem_wid - object_wid
		
		return number_of_sheets

if __name__ == "__main__":
	objects = [[10, 20], [400, 300], [200, 400], [100, 100], [200, 300], [400, 400], [100, 100], [900, 800]]
	sheet_dimensions = [800, 800]
	# A = []
	sol = Solution()
	out = sol.solve(objects, sheet_dimensions)
	pass