'''nums = [100, 4, 200, 1, 3, 2]. 
The longest consecutive sequence is [1, 2, 3, 4] 
with length 4.'''


def longest_sequence(nums):
    max_length = 0
    if type(nums) != list:
        return 0
    if len(nums) < 2:
        return len(nums)
    nums_set = set(nums)
    for num in nums_set:
        if num - 1 in nums_set:
            continue
        curr_num = num
        curr_length = 0
        while curr_num in nums_set:
            curr_length += 1
            if curr_length > max_length:
                max_length = curr_length
            curr_num = curr_num + 1
    return max_length


if __name__ == '__main__':
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    longest_sequence(nums)
