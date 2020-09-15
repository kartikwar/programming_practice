"""
Pair of indices to satisfy the Smallest subsequence.
Input:  abdc, bd    Output: 2
"""



class Solution:
	
	#start_idx	is the index of the first word in line
	#end_idx is the index of the last word in line
	def arrange_space(self, words, start_idx, end_idx, spaces):
		word_cnt = end_idx - start_idx + 1
		line = ""
		if word_cnt == 1:
			line += words[start_idx]
			line += " " * spaces
			return line
		evenly_dist = spaces // (word_cnt - 1)
		extra_spaces = spaces % (word_cnt - 1)
		for word_ind in range(start_idx, end_idx + 1):
			line += words[word_ind]
			
			#last line pad extra spaces to the right
			if end_idx == len(words) - 1 and spaces > 0:
				line += " "
				spaces -= 1
				#pas all the spaces after the last word
				if word_ind == end_idx:
					for i in range(spaces):
						line += " "
			else:
				#pad extra spaces to the left
				if word_ind != end_idx:
					for i in range(evenly_dist):
						line += " "
					if extra_spaces > 0:
						line += " "
						extra_spaces -= 1
		return line
	
	def fullJustify(self, words, L):
		total_words = len(words)
		ans = []
		word_index = 0
		while word_index < total_words:
			word_count = 0
			width = 0
			start_idx = word_index
			while word_index < total_words:
				width += len(words[word_index])
				word_count += 1
				if width + word_count - 1 <= L:
					word_index += 1
				else:
					width -= len(words[word_index])
					word_count -= 1
					break
			end_idx = word_index - 1
			line = self.arrange_space(words, start_idx, end_idx, L - width)
			ans.append(line)
		return ans
		
if __name__ == "__main__":
	words = ["This", "is", "also", "aan", "example", "of", "text", "justification."]
	L = 16
	sol = Solution()
	out = sol.fullJustify(words, L)
	pass