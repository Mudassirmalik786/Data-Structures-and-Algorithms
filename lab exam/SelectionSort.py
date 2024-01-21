import random
import time
import csv

def SelectionSort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
          
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

# Simple sorted array using selection sort

Arr = [2, 5, 1, 7, 6]
sortedArr = SelectionSort(Arr)
print("Sorted Array is:", sortedArr)
 
# Saving Sorted array in sorted selection csv file

sorted_filename = "SortedSelectionSort.csv"

with open(sorted_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for num in Arr:
        writer.writerow([num])

# Random array of 30000 integers sorted by this function

randomArr = [random.randint(1, 100000) for i in range(30000)]
sortedArr = SelectionSort(randomArr.copy())
print("Sorted Array of 30000 integers are:", sortedArr)

# Measuring Time

startTime = time.time()
sortedArr = SelectionSort(randomArr.copy())
endTime = time.time()
totalTime = endTime - startTime
print("Time for sorted arrays is:", totalTime, "Seconds")
