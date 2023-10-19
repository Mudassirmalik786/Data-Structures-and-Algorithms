# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:18:41 2023

@author: HP
"""

# Problem 1


import random
import time
def RandomArray(size):
    if size <= 0:
        raise ValueError("Size must be a positive integer.")
        
    random_array = [random.randint(1, 100) for _ in range(size)]
    return random_array

# Sorting Algorithms code written using their pseudo code

def InsertionSort(array, start, end):
    for j in range(start + 1, end):
        key = array[j]
        i = j - 1
        while i >= start and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key

def MergeSort(array, start, end):
    if start < end:
        middle = (start + end) // 2
        MergeSort(array, start, middle)
        MergeSort(array, middle + 1, end)
        Merge(array, start, middle, end)

def Merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    left_subarray = array[p:p + n1]
    right_subarray = array[q + 1:q + 1 + n2]

    i = j = 0
    k = p

    while i < n1 and j < n2:
       if left_subarray[i] <= right_subarray[j]:
           array[k] = left_subarray[i]
           i += 1
       else:
           array[k] = right_subarray[j]
           j += 1
       k += 1

    while i < n1:
       array[k] = left_subarray[i]
       i += 1
       k += 1

    while j < n2:
       array[k] = right_subarray[j]
       j += 1
       k += 1

def HybridMergeSort(array, start, end, n):
    if start < end:
        if end - start + 1 <= n:
            InsertionSort(array, start, end - 1)  
        else:
            middle = (start + end) // 2
            HybridMergeSort(array, start, middle, n)
            HybridMergeSort(array, middle + 1, end, n)
            Merge(array, start, middle, end)

def BubbleSort(array, start, end):
    for i in range(start, end):
        for j in range(start, end - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

def SelectionSort(array, start, end):
    for j in range(start, end):
        smallest = j
        for i in range(j, end):
            if array[i] < array[smallest]:
                smallest = i
        array[j], array[smallest] = array[smallest], array[j]

def ShuffleArray(array, start, end): # This function will use in problem 8
    random.shuffle(array[start:end + 1])

def measure_sorting_time(sort_function, array, start, end, n=None): #This function will use in problem 7
    start_time = time.time()
    if n is not None:
        sort_function(array, start, end, n)
    else:
        sort_function(array, start, end)
    end_time = time.time()
    return end_time - start_time

# Main Program
randomArray_size = 10
randomArray = RandomArray(randomArray_size)
print("Random Array: ",randomArray) 
