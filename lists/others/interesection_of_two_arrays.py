"""
find the interesection of two lists
for ex:- 
Input : 
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
Output :
[9, 10, 4, 5]
"""

#time complexity is 0(n^2)
def find_interesection(lst1, lst2):
    # return [ele for ele in lst1 if ele in lst2]
    result = []
    for ele in lst1:
        if ele in lst2:
            if ele not in result:
                result.append(ele)
    return result

def binary_search(ele, lst):
    found = False
    start = 0
    end = len(lst) -1
    while start <= end:
        index = int((start + end)/2)
        if ele < lst[index]:
            end = index -1
        elif ele > lst[index]:
            start  = index + 1
        else:
            found = True
            break
    return found

#time complexity is 0(nlogn)
def find_interesection(lst1, lst2):
    # return [ele for ele in lst1 if ele in lst2]
    result = []
    
    lst1 = sorted(lst1)
    lst2 = sorted(lst2)

    for ele in lst1:
        if binary_search(ele, lst2):
            if ele not in result:
                result.append(ele)
    
    return result


#time complexity is 0(n)
def find_interesection(lst1, lst2):
    # return [ele for ele in lst1 if ele in lst2]
    result = []
    
    # lst1 = sorted(lst1)
    # lst2 = sorted(lst2)

    lookup = {}

    for ele in lst2:
        if ele not in lookup:
            lookup[ele] = 0
    

    for ele in lst1:
        if ele in lookup:
            # if ele not in result:
                result.append(ele)
    
    return list(set(result))


if __name__ == '__main__':
    lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
    lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
    output = find_interesection(lst1, lst2)
    print(output)