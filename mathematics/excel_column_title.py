'''
Given a positive integer A, 
return its corresponding column title 
as appear in an Excel sheet.

Input 1:
A = 1

Output 1:
 "A"

Input 2:
A = 28

Output 2:
 "AB"

'''

class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        result = []
        
        #bit = len(result)
        while A > 0:
            
            bit_val = A % 26
            if bit_val == 0:
                bit_val = 26
                
            #print(A, bit_val)
            
            A = (A) // 26  
            result.append(chr(bit_val + 64))
            
        return ''.join(reversed(result))

if __name__ == '__main__':
    sol = Solution()
    print(sol.convertToTitle(A=943566))