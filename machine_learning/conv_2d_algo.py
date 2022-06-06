'''
to do:- make image and kernel as 2d numpy arrays 
and then do it
'''

def convolution2d(image, kernel):
    out = None
    K = len(kernel)
    I = len(image)
    output = []
    for i in range(0, I , I - K):
        outj = []
        for j in range(0, I, I - K):
            # outj = []
            for k in range(K):
                res = image[i][j] * kernel[k]
                outj.append(res)
            temp = 0
        # outi.append(outj)
        output.append(outj)
    return output


if __name__ == '__main__':
    image = [[1,2], [2,3]]
    kernel = [2]
    print(convolution2d(image, kernel))