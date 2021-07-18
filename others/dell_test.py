import numpy as np

import pandas as pd

def solution():
	print('started soln')
	return 1 



if __name__ == "__main__":

	a = np.array ([1,2,3])

	b = np.arange(3)

	c = a * b

	d = np.array([[1,2], [5, 6]])

	e = np.sum(d, axis = 1)

	week = pd.Series({'a' : 'abc', 'b' : 'def', 'c' : 'ghi'})

	print(week['a' : 'b'])

	print(week[[0,1]])

	print(week[:2])

	a = pd.Series([1,2,3])

	b = a[:2]


	temp = 0