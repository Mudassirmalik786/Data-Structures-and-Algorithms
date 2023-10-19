# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 01:12:20 2023

@author: HP
"""
import random
import csv
from funcs import HybridMergeSort


def RandomArray(size):
    if(size<=0):
        raise ValueError("Size must be a positive integer.")
        
    random_array = [random.randint(1, 30000) for i in range(size)]
    return random_array
 
arr = [12, 11, 13, 5, 6, 7, 4, 8, 10, 9]
print("Original array:", arr)

HybridMergeSort(arr, 0, len(arr) - 1, n=1)
#print("Sorted array:", arr)

arr_Size = 30000
random_array = RandomArray(arr_Size)
HybridMergeSort(random_array, 0, arr_Size - 1, n=1)
print("Sorted Random Array: ", random_array[:15])

with open('SortedHybridSort.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for num in random_array:
            writer.writerow([num])

print("The random array has been saved in file")