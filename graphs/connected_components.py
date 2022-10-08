'''https://www.interviewbit.com/problems/connected-components/'''
# from sklearn import neighbors
# import re

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, e):
        n=A
        g=[[] for i in range(n+1)]
        for i in e:
            g[i[0]].append(i[1])
            g[i[1]].append(i[0])
        vis=[False]*(n+1)
        c=0
        # ans = []
        for curr in range(1,n+1):
            if vis[curr] == False:
                stack=[]
                stack.append(curr)
                while(stack):
                    curr=stack.pop()
                    if vis[curr] == False:
                        # ans.append(curr)
                        vis[curr] = True
                        for i in g[curr]:
                            stack.append(i)
                c+=1
        return (c)



if __name__ == '__main__':
	sol = Solution()
	A = 100
	B = "[14, 1] [46, 76] [22, 54] [68, 5] [94, 68] [52, 39] [4, 84] [53, 6] [1, 68] [7, 39] [69, 42] [94, 59] [53, 85] [66, 10] [71, 42] [77, 92] [5, 27] [33, 74] [76, 64] [37, 100] [99, 25] [76, 73] [8, 66] [89, 64] [44, 28] [48, 77] [28, 24] [17, 36] [90, 49] [7, 91] [51, 91] [32, 52] [50, 99] [10, 27] [8, 95] [39, 51] [92, 28] [47, 53] [6, 95] [78, 77] [13, 83] [69, 2] [63, 87] [73, 74] [89, 100] [31, 24] [52, 36] [85, 60] [85, 42] [42, 27] [47, 54] [18, 29] [58, 16] [4, 81] [50, 54] [75, 96] [90, 56] [85, 63] [22, 16] [14, 72] [28, 10] [42, 1] [71, 3] [24, 94] [32, 19] [66, 89] [69, 16] [39, 39] [15, 50] [85, 59] [96, 60] [15, 56] [41, 99] [57, 15] [49, 26] [97, 47] [20, 13] [63, 32] [66, 13] [81, 63] [48, 25] [21, 39] [91, 3] [15, 43] [42, 95] [89, 14] [17, 10] [37, 8] [14, 26] [46, 79] [46, 35] [94, 81] [22, 66] [91, 68] [87, 26] [51, 48] [82, 61] [47, 76] [64, 96] [83, 44] [71, 69] [96, 99] [29, 86] [52, 54] [42, 11] [88, 58] [73, 45] [72, 87] [71, 81] [2, 75] [53, 89] [7, 47] [49, 72] [69, 67] [92, 20] [90, 87] [14, 55] [99, 46] [45, 22] [52, 32] [44, 89] [81, 47] [22, 37] [16, 100] [62, 64] [1, 1] [73, 78] [42, 32] [69, 69] [84, 21] [83, 71] [9, 10] [63, 77] [22, 22] [39, 9] [95, 96] [27, 39] [29, 70] [79, 78] [29, 43] [2, 20] [99, 20] [82, 25] [40, 14] [18, 61] [16, 83] [26, 99] [11, 24] [64, 22] [80, 70] [76, 70] [64, 67] [60, 6] [32, 23] [12, 70] [53, 77] [59, 56] [71, 33] [17, 15] [87, 49] [56, 82] [32, 74] [53, 14] [59, 32] [44, 52] [38, 26] [45, 40] [39, 48] [8, 28] [26, 37] [68, 68] [73, 52] [95, 73] [95, 47] [47, 33] [67, 52] [61, 41] [16, 99] [35, 68] [53, 55] [2, 83] [65, 28] [92, 55] [98, 27] [85, 25] [46, 70] [3, 82] [71, 17] [44, 71] [76, 59] [70, 100] [76, 28] [1, 18] [8, 50] [91, 17] [75, 79] [1, 44] [52, 59] [55, 7] [22, 39] ]"
	# B = B.split(" ")
	reg = r'[0-9]+\s*,\s[0-9]+'
	B = re.findall(reg, B)
	out = []
	for ele in B:
		# out.append()
		ele = ele.split(', ')
		outer = [int(ele[0]), int(ele[1])]
		out.append(outer)
		temp = 0
	print(sol.solve(A, out))