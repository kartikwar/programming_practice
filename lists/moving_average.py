"""
Given a list return a list containing moving average of the elements
For example:
input = [10,20,30,10]
output= [10,15,20,17.5]
"""

def calculate_average(data):
    moving_list = []
    counter = 1
    sum = 0
    for ele in input:
        sum = sum + ele
        mov_avg = sum/counter
        counter += 1
        moving_list.append(mov_avg)
    return moving_list

if __name__ == '__main__':
    input = [10,20,30,10]
    output = calculate_average(input)    
    print(output)