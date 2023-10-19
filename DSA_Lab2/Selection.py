# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 01:48:11 2023

@author: HP
"""
from funcs import SelectionSort
import random
import time
import csv
array = [10, 7 ,6, 9, 12]
SelectionSort(array, 0, len(array))
print("Sorted array", array)

def RandomArray(size):
    if(size<=0):
        raise ValueError("Size must be a positive integer.")
        
    random_array = [random.randint(1, 30000) for i in range(size)]
    return random_array

arr_size = 30000
random_array = RandomArray(arr_size)
start_time = time.time()
SelectionSort(random_array, 0, len(random_array))
end_time = time.time()
runtime = end_time - start_time
print("The sorted array of 30000 random integers is:", random_array[:12])
print("The running time of selection sort is: ", runtime, "seconds")

with open('SortedSelectionSort.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for num in random_array:
            writer.writerow([num])

print("The random array has been saved in file")