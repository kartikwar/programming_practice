'''
Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.
'''

class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution:
# @param intervals, a list of Intervals
# @return a list of Interval
	def merge(self, intervals):
		intervals = sorted(intervals, key=lambda y:y.start)
		i = 0

		while i < len(intervals) -1:
			ele1, ele2 = intervals[i], intervals[i+1]
			a,b = ele1.start, ele1.end
			c,d = ele2.start, ele2.end
			if max(a,c) > min(b,d):
				i = i +1
			else:
				intervals[i] = Interval(min([a,c]), max(b,d))
				intervals.pop(i+1)

		return intervals


if __name__ == '__main__':
	sol = Solution()
	A = [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]
	intervals = []
	for a in A:
		intervals.append(Interval(a[0], a[1]))
	print(sol.merge(intervals))