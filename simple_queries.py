import math

class Solution:

	def union(self, ele):
		clone = []

		for existing_ele in self.subarrays:
			# ele_array = [ele]
			if not len(self.subarrays):
				clone.append(ele)
			elif ele > existing_ele:
				clone.append(ele)
			else:
				continue
		
		self.subarrays = self.subarrays + clone
	
	def get_divisors(self, number):
		divisors = []
		product = 1
		for i in range(1, int(math.sqrt(number)) + 1) :
			if number % i == 0:
				if number/i not in divisors:
					divisors.append(number/i)
				if i not in divisors:
					divisors.append(i)
		for ele in divisors:
			product *= int(ele)

		return product

	def generate_subarrays(self):
		self.subarrays = [-1]
		# leave = index = 0
		
		for ele in self.A:
			self.union(ele)
		
		self.subarrays = self.subarrays[1:]

	
	def generate_G(self):
		divisors = []
		self.G = self.subarrays
		# for sublist in self.subarrays:
		# 	self.G.append(max(sublist))

		unique_G = []

		for index, ele in enumerate(self.G):
			if ele not in unique_G:
				unique_G.append(ele)
		
		divisors_map = {}

		for ele in unique_G:
			divisors_map[ele] = self.get_divisors(ele)

		for index,ele in enumerate(self.G):
			self.G[index] = divisors_map[ele]

		self.G = sorted(self.G, reverse=True)
		return self.G

	def perform_queries(self):
		for i, query in enumerate(self.B):
			self.B[i] = self.G[query]
		return self.B

	# @param A : list of integers
	# @param B : list of integers
	# @return a list of integers
	def solve(self, A, B):
		self.A = A
		self.B = B
		self.G = []
		self.generate_subarrays()
		self.generate_G()
		self.perform_queries()
		return self.B

if __name__ == "__main__":
	A =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
	B  = [ 2775, 2774, 2773, 2772, 2771, 2770, 2769, 2768, 2767, 2766, 2765, 2764, 2763, 2762, 2761, 2760, 2759, 2758, 2757, 2756, 2755, 2754, 2753, 2752, 2751, 2750, 2749, 2748, 2747, 2746, 2745, 2744, 2743, 2742, 2741, 2740, 2739, 2738, 2737, 2736, 2735, 2734, 2733, 2732, 2731, 2730, 2729, 2728, 2727, 2726 ]

	# A = [1,2,4]
	# B = [0,1,2]

	sol = Solution()
	out = sol.solve(A=A, B=B)
	pass