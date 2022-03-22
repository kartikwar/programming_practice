"""
Given a collection of numbers, return all possible permutations.

Example:
[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3] 
[2,3,1] 
[3,1,2] 
[3,2,1]
"""



def gen_perms(A):
    result = []
    if len(A) == 1:
        return [A]
    for i  in range(len(A)):
        sub_groups = gen_perms(A[:i] + A[i+1:])
        perms = [[A[i]] + sub_group for sub_group in sub_groups]
        # print(perms)
        result.extend(perms)

    return result


if __name__ =='__main__':
    result =  gen_perms([1,2,3])
    print(result)