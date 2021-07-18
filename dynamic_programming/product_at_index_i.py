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
    forward_product = [1]* len(values)
    backward_product = [1]* len(values)

    for i, value in enumerate(values):
        if i >0:
            forward_product[i] = forward_product[i-1] * values[i-1]
    
    values = list(reversed(values))

    for i, value in enumerate(values):
        if i >0:
            backward_product[i] = backward_product[i-1] *values[i-1]
    
    backward_product = list(reversed(backward_product)) 
    
    return [forward_product[i] * backward_product[i] for i in range(len(forward_product))]



if __name__ == '__main__':
    values = [1,2,3,4 ,5]
    output = product_on_index(values)
    temp = 0


