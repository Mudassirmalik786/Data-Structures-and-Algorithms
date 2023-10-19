# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:02:39 2023

@author: HP
"""
#Function in python
def SearchA(arr,x):
    indices = []
    for i in range(len(arr)):
        if arr[i] == x:
            indices.append(i)
    return indices
#main program
arr = [22, 2, 1, 7, 11, 13, 5, 2, 9]
x = int(input("Enter a number you want to search: "))
indices = SearchA(arr, x)
if indices:
    print("Index:", ', '.join(map(str, indices)))
else:
    print("Number not present")

        
        