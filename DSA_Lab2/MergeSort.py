# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 23:14:20 2023

@author: HP
"""
import random
import time
import csv
from funcs import MergeSort

# main Function
arr = [13, 12, 6, 8, 10]
#print("Unsorted array", arr)

MergeSort(arr, 0, len(arr) - 1)
print("Sorted Array", arr)

# Merge Sort 2nd Point
def RandomArray(size):
    if(size<=0):
        raise ValueError("Size must be a positive integer.")
        
    random_array = [random.randint(1, 30000) for i in range(size)]
    return random_array

arr_size = 30000
random_array = RandomArray(30000)
start_time = time.time()
MergeSort(random_array, 0, arr_size - 1)
end_time = time.time()
runtime = end_time - start_time
print("The time taken by MergeSort Function is",runtime," seconds")
print("Sorted array of random 30000 integers as folows: ", random_array[:20])
# Output taken by merge sort funtion is :
# The time taken by MergeSort Function is 0.2149956226348877  seconds
with open('SortedMergeSort.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for num in random_array:
            writer.writerow([num])

print("The random array has been saved in file")