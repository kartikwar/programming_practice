"""
Write a Python function that displays the first n Fibonacci numbers
for ex: 
input:- 
n = 5
output:
result = [0,1,1,2,3]
"""

def fib_list(n):
    result = []
    for i in range(n):
        if i < 2:
            result.append(i)
        else:
            result.append(result[i-1] + result[i-2])
    return result

if __name__ == '__main__':
    print(fib_list(6))