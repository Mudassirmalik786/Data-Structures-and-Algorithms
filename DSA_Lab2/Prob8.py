# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 12:55:34 2023

@author: HP
"""
from funcs import InsertionSort, MergeSort, measure_sorting_time, ShuffleArray

def ReadWordsFromFile(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    return words

file_path = 'words.txt'
words = ReadWordsFromFile(file_path) #The Functions will return words which can be entered in words variable

insertion_sort_time = measure_sorting_time(InsertionSort, words.copy(), 0, len(words))

merge_sort_time = measure_sorting_time(MergeSort, words.copy(), 0, len(words)-1)

print("Runtime of Insertion Sort is",insertion_sort_time,"seconds")
print("Runtime of Insertion Sort is",merge_sort_time,"seconds")

ShuffleArray(words, 0, len(words)-1)

shuffling_insertionsort_time = measure_sorting_time(InsertionSort, words.copy(), 0, len(words))
shuffling_mergesort_time = measure_sorting_time(MergeSort, words.copy(), 0, len(words)-1)

print("The time taken by Inssertion sort for shuffling words array is:",shuffling_insertionsort_time,"seconds")
print("The time taken by Merge sort for shuffling words array is:",shuffling_mergesort_time,"seconds")

#Question's Answer

print("Yes! Shuffling of array can impact the runtime of sorting algorithms")

