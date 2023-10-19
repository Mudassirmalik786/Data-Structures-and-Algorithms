# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:25:14 2023

@author: HP
"""

def insertion_sort(arr):
    n = len(arr)
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key

# Example usage
A = [5, 2, 4, 6, 1, 3]
insertion_sort(A)
print("Sorted array:", A)