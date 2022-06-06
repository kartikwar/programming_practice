'''
implement a convolutional 2d algorithm
using only numpy and lists
'''

import numpy as np


def convolution2d(image, kernel):
    K = kernel.shape[0]
    I = image.shape[0]
    output = []
    for i in range(0, I-K+1):
        outj = []
        for j in range(0, I-K+1):
            res = np.sum(image[i:i+K, j:j+K] * kernel)
            outj.append(res)

        output.append(outj)

    return np.array(output)


if __name__ == '__main__':
    image = np.array([[1,2,3], [2,3,4], [3,4,5]])
    kernel = np.array([[1,1,1,1], [2,2,2,2], [3,3,3,3], [4,4,4,4]])  
    out = convolution2d(image, kernel)
    temp = 0