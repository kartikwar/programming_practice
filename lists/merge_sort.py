class Solution:

	def merge_sort(self, a):
		if len(a) > 1:
			left_arr = a[:len(a)//2]
			right_arr = a[len(a)//2:]
			
			#recursively sort till one element 
			#is left, array is sorted with one element
			self.merge_sort(left_arr)
			self.merge_sort(right_arr)

			#start merging left and right arrays
			i = 0 # index of left array
			j = 0 # index of riht array
			k = 0 #index of merged array

			while i < len(left_arr) and j < len(right_arr):
				#compare
				if left_arr[i] > right_arr[j]:
					a[k] = right_arr[j]
					j += 1
				else:
					a[k] = left_arr[i]
					i += 1
				k += 1

			# if left_arr was exhausted
			while j < len(right_arr):
				a[k] = right_arr[j]
				k += 1
				j += 1

			# if right_arr was exhausted
			while i < len(left_arr):
				a[k] = left_arr[i]
				k += 1
				i += 1

if __name__ == "__main__":
	A = [9, 6,2, 1, 7, 8, 5]
	sol = Solution()
	sol.merge_sort(A)
	print(A)