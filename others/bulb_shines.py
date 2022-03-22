"""
A - array of bulbs. A[i] its position in row.
return number of moments where all turned on bulbs are shined
start from 0 to length-1, switch on bulbs ( A[i] represents a bulb's position)
A[i] bulb shined if: 1) A[i] is switched 2) 1..A[i]-1 all are shined
examples:
input: {1,2,3,4,5} output: 5
input: {1} output: 1
input: {2,3,4,1,5} output: 2
input: {2,1,3,5,4} output: 3
"""

def solution(a):
    count = 0
    #missing previous bulbs that need to be encountered
    missing = set()
    #set of bulbs that were switched on, but didnt shine
    store = set()

    for i in range(len(a)):
        if i+1 not in store:
            if i +1 != a[i]:
                missing.add(i+1)
        if i+1 < a[i]:
            store.add(a[i])
        else:
            if a[i] in missing:
                missing.remove(a[i])

        if len(missing) == 0:
            count = count + 1

    return count


if __name__ == '__main__':
    a = [5,4,3,2,1]
    print(solution(a))