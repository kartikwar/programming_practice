"""
Problem Link:- https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
"""

from collections import Counter

# Solution using lookup
# time:- complexity O(m+n), Space Complexity:- O(min(n,m))


def intersect(nums1, nums2):
    counts = Counter(nums1)
    result = []

    for num in nums2:
        if counts[num] > 0:
            result.append(num)
            counts[num] -= 1

    return result

# Solution with sorting
# Time Complexity:- O(n log n + m log m), Space Complexity:- O(1)


def intersect(nums1, nums2):
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)

    i = 0
    j = 0

    result = []

    while (i < len(nums1)) and (j < len(nums2)):
        num1 = nums1[i]
        num2 = nums2[j]

        if num1 == num2:
            i += 1
            j += 1
            result.append(num1)

        elif num1 > num2:
            j += 1

        else:
            i += 1

    return result


if __name__ == '__main__':
    lst1 = [1, 2, 2, 1]
    lst2 = [2]
    output = intersect(lst1, lst2)
    print(output)
