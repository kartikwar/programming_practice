def q_sort(values):
    start = 0
    end = len(values) -1

    pivot = None

    if len(values) < 2:
        return values
    
    elif len(values) == 2:
        if values[0] > values[1]:
            values[0], values[1] = values[1], values[0]
        return values

    pivot = values[start]
 
    while start < end:

    #find first greater value:
        while start < len(values) - 1:
            if values[start] > pivot:
                break
            else:
                start = start + 1

    #find first smaller value
        while end > 0:
            if values[end] <= pivot:
                break
            else:
                end = end - 1

        # compare start and end values and swap if needed

        if start!=0 and end!=0 and start< end:
            values[start], values[end] = values[end], values[start]

        else:
            break
    
    #swap pivot and end index
    if end > 0:
        values[0], values[end] = values[end], values[0]

    partition_index = end

    left_array, right_array = [], []

    if partition_index > 0:
        left_array = values[:partition_index] 
        right_array = values[partition_index + 1:]
        values = q_sort(left_array) + [values[partition_index]] + q_sort(right_array) 
    else:
        left_array = values[:1]
        right_array = values[1:]
        values = left_array + q_sort(right_array)

    return values

if __name__ == '__main__':
    values = [7,6,10,5,9,2,1,15,7]
    print(q_sort(values))