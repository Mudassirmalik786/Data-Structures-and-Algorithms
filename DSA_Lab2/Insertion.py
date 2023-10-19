# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 23:13:06 2023

@author: HP
"""
from funcs import InsertionSort
# Insertion sort 1st point
array = [9, 7, 3, 1, 2]
start = 0
end = 5
sorted_array = InsertionSort(array, start, end)
print("Sorted array: ", array)


# Insertion sort 2nd point
import random
import time
import csv
def RandomArray(size):
    return [random.randint(1, 30000) for i in range(size)]


array_size = 30000
random_array = RandomArray(array_size)
start_time = time.time()
sorted_array = InsertionSort(random_array, 0, array_size - 1)
end_time = time.time()
print("sorted array of random 30000 integers", sorted_array[:12])

#Insertion Sort Third Point
runtime = end_time - start_time
print("Time taken by Insertion sort function is: ", runtime, " seconds")
# Output of above whole code is
# sorted array of random 30000 integers [1, 1, 3, 6, 8, 8, 8, 8, 8, 9, 13, 13]
# Time taken by Insertion sort function is:  55.14812421798706

# Insertion Sort 4rth Point
with open('SortedInsertionSort.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for num in sorted_array:
            writer.writerow([num])

print("The array has been saved in file")