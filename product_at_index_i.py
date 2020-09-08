"""
Given an array arr[] of n integers,
construct a Product Array prod[] (of same size) such
that prod[i] is equal to the product of all the elements of arr[] except arr[i].
Solve it without division operator in O(n) time.

values = [1,2,3,4,5]

output = [120, 60, 40, 30,  24]

asked in cimpress coding round(3)

part of dynamic programming
"""

def product_on_index(values):
    output = []
    
    out1 = list(range(len(values)))
    out1[0] = 1
    out1[1] = values[0]
    
    for ind in range(1, len(values)):
        out1[ind] = out1[ind-1] * values[ind -1]


    values = values[::-1]
    
    out2 = list(range(len(values)))
    out2[0] = 1
    out2[1] = values[0]
    
    for ind in range(1, len(values)):
        out2[ind] = out2[ind-1] * values[ind -1]
    
    out2 = out2[::-1]
   
    for ind in range(len(out1)):
        output.append(out1[ind] * out2[ind])

    return output
    
    # temp = 0
    

# def fn_neural():
#     input = [[0,0,1], [0,1,1], [1, 0,1], [1,1,1]]
#
#     y = [0,1,1,0]
#
#     #output would be 2 units
#
#     #loss would be sigmoid and then just do mean square
#
#     """
#     input -> hidden layer(3 nodes) -> weights [-1, 0,1]
#     """
#
#     weights = np.random(shape=(4,))
#
#     total_loss = 0
#
#     for index, inp_ in  enumerate(input):
#         out = np.softmax(inp_ * weights)
#         loss = (y[index] - out)^2
#         total_loss += loss
#
#     np
    
    #1 input, 1 hidden, 1 output

    
    



if __name__ == '__main__':
    # print_hi('PyCharm')
    values = [1,2,3,4 ,5]
    product_on_index(values)


