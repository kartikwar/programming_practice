"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
There might be multiple gray code sequences possible for a given n.

Return any such sequence.

Note :- backtracking algos generally have a time and space complexity of (2^N)

"""

def grayCode(A):
    curr = ['0','1']
    for i in range(2, A+1):
        L1 = curr
        L2 = curr[::-1]
        L1 = ['0' + ele for ele in L1]
        L2 = ['1' + ele for ele in L2]
        curr = L1 + L2
    curr = [int(ele, 2) for ele in curr]
    return curr

if __name__ == '__main__':
    print(grayCode(2))