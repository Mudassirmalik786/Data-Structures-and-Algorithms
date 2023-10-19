# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 01:48:11 2023

@author: HP
"""
import random
import time
import csv
from funcs import BubbleSort
    
# main function
array = [10, 7 ,6, 9, 12]
BubbleSort(array, 0, len(array))
print("Sorted Array: ", array)

def RandomArray(size):
    if(size<=0):
        raise ValueError("Size must be a positive integer.")
        
    random_array = [random.randint(1, 30000) for i in range(size)]
    return random_array

array_size = 30000
random_array = RandomArray(array_size)
start_time = time.time()
BubbleSort(random_array, 0, len(random_array))
end_time = time.time()
runtime = end_time - start_time
print("Sorted array", random_array[:12])
print("The time taken by bubble sort is ",runtime," seconds")
with open('SortedBubbleSort.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for num in random_array:
            writer.writerow([num])

print("The random array has been saved in file")
#Output of above code
#Sorted Array:  [6, 7, 9, 10, 12]
#Sorted array [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#The time taken by bubble sort is  133.4137704372406  seconds

