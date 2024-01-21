import random
import time
import csv

def BubbleSort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# Simple sorted array using bubble sort

Arr = [3, 5, 6, 4, 7]
sortedArr = BubbleSort(Arr)
print("Sorted Array is:", sortedArr)

# Saving Sorted array in sorted BubbleSelection csv file

sorted_filename = "SortedBubbleSort.csv"

with open(sorted_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for num in Arr:
        writer.writerow([num])

# Random array of 30000 integers sorted by this function

randomArr = [random.randint(1, 100000) for i in range(30000)]
sortedArr = BubbleSort(randomArr.copy())
print("Sorted Array of 30000 integers are:", sortedArr)

# Measuring Time
startTime = time.time()
sortedArr = BubbleSort(randomArr.copy())
endTime = time.time()
totalTime = endTime - startTime
print("Time for sorted arrays is:", totalTime, "Seconds")
