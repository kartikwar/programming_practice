"""
Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value.
Report the minimum XOR value.
"""

def min_xor(A):
    
    return A[0] ^ A[1]



if __name__ == '__main__':
    A = [0,4,7,9]
    out = min_xor(A)
    print(out)