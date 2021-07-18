"""
If given an integer n and an array of numbers, create a histogram divided into n bins

for ex: 
lst = [15, 9, 10, 56, 23, 78, 5, 4, 9]
n = 3
result = [[4,5,9,9], [10,15,23], [56,78]]

out = [4,5,9,9,10,15,23,56,78]
"""

from matplotlib import pyplot as plt
import math

def split_in_bins(data, bins):
    plt.hist(data, bins=3)
    plt.show()

def split_in_bins(data, bins):
    width = math.ceil((max(data) - min(data))/bins)
    # result = [[4]*bins]
    result = []
    for i in range(bins):
        result.append([])
    for ele in data:
        bin_number = int(ele / width)
        if bin_number > bins -1:
            bin_number = bins -1
        result[bin_number].append(ele)
    return result 

if __name__ == '__main__':
    data = [15, 9, 10, 56, 23, 5, 4, 9]
    split_in_bins(data, 3)
    

