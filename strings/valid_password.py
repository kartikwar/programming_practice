'''
Given a password as a character array A.
Check if it is valid or not.
Password should have at least one numerical digit(0-9).
Password's length should be in between 8 to 15 characters.
Password should have at least one lowercase letter(a-z).
Password should have at least one uppercase letter(A-Z).
Password should have at least one special character ( @, #, %, &, !, $, ., *)
'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        len_cond = False
        numerical_cond = False
        lower_cond = False
        upper_cond = False
        special_cond = False

        special_chars = ['@', '#', '%', '&', '!', '$' , '.', '*']

        if len(A) > 7 and len(A) < 16:
            len_cond = True
            for char in A:
                if char.isdigit():
                    numerical_cond = True
                if char.islower():
                    lower_cond = True
                if char.isupper():
                    upper_cond = True
                if char in special_chars:
                    special_cond = True        

        result = len_cond and numerical_cond and lower_cond and upper_cond and special_cond
        return  int(result)