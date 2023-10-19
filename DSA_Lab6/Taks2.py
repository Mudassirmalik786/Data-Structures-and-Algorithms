# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:17:27 2023

@author: HP
"""
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 20  # Count for digits from -9 to 9

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index + 10] += 1

    for i in range(1, 20):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index + 10] - 1] = arr[i]
        count[index + 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # Separate negative and positive numbers
    negative_nums = [x for x in arr if x < 0]
    positive_nums = [x for x in arr if x >= 0]

    # Sort the absolute values of positive numbers using radix sort
    max_num = max(positive_nums, key=abs)
    exp = 1
    while max_num // exp > 0:
        counting_sort(positive_nums, exp)
        exp *= 10

    # Sort the absolute values of negative numbers using radix sort
    max_num = max(negative_nums, key=lambda x: abs(x))
    exp = 1
    while abs(max_num) // exp > 0:
        counting_sort(negative_nums, exp)
        exp *= 10

    # Reverse the negative numbers to get them in descending order
    negative_nums.reverse()

    # Merge the sorted negative and positive numbers
    sorted_arr = negative_nums + positive_nums
    return sorted_arr

arr = [170, -45, 75, -90, -802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print("Original array:", arr)
print("Sorted array:", sorted_arr)

