'''
Problem Description

Given two integer array A and B, you have to pick one element 
from each array such that their xor is maximum.

Return this maximum xor value.

Problem Constraints
1 <= |A|, |B| <= 105

1 <= A[i], B[i] <= 109



Input Format
First argument is an integer array A.

Second argument is an integer array B.



Output Format
Return an integer denoting the maximum xor value as described in the question.



Example Input
Input 1:

 A = [1, 2, 3]
 B = [4, 1, 2]


Example Output
Output 1:

 7


Example Explanation
Explanation 1:

 Pick A[2] and B[0] because their xor value is maximum. 3 ^ 4 = 7
'''


import math


class TrieNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Trie:
    def __init__(self):
        node = TrieNode('*')
        self.root = node
    
    def insert_node(self, value):
        curr_node = self.root
        for i in range(31, -1, -1):
            curr_bit = (value >> i) & 1
            if curr_bit == 0:
                if curr_node.left == None:
                    node = TrieNode(0)
                    curr_node.left = node
                
                curr_node = curr_node.left
            else:
                if curr_node.right == None:
                    node = TrieNode(1)
                    curr_node.right = node
                
                curr_node = curr_node.right
    
    def max_xor_value(self, value):
        xor_value = 0
        curr_node = self.root
        
        for i in range(31, -1, -1):
            curr_bit = (value >> i) & 1
            if curr_bit == 0:
                if curr_node.right != None:
                    xor_value += math.pow(2,i)
                    curr_node = curr_node.right
                else:
                    curr_node = curr_node.left        
                
            else:
                if curr_node.left != None:
                    xor_value += math.pow(2,i)
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right

        return int(xor_value)

def solve(A, B):
    tree = Trie()

    for number in A:
        tree.insert_node(number)
    
    max_xor = 0

    for num in B:
        curr_xor = tree.max_xor_value(num)
        if curr_xor > max_xor:
            max_xor = curr_xor

    return max_xor

if __name__ == '__main__':
    A = [1, 2, 3]
    B = [4, 1, 2]
    print(solve(A, B))