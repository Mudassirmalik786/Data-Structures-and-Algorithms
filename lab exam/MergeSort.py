import random
import time
import csv

def MergeSort(array, start, end):
    if start < end:
        mid = (start + end) // 2
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        Merge(array, start, mid, end)
     

def Merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    # Create temporary arrays
    left = [0] * n1
    right = [0] * n2

    for i in range(n1):
        left[i] = array[p + i]
    for j in range(n2):
        right[j] = array[q + j + 1]

    i = j = 0
    k = p
    
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = right[j]
        j += 1
        k += 1
                       
    # Saving Sorted array in sorted MergeSelection csv file

    sorted_filename = "SortedMergeSort.csv"
    with open(sorted_filename, 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)
    for num in array:
          writer.writerow([num])    

def RandomArray(size):
    return [random.randint(1, 100000) for _ in range(size)]

# Create a random array of 30,000 integers
randomArr = RandomArray(30000)

# Measure the time taken to sort the array using Merge Sort
startTime = time.time()
MergeSort(randomArr, 0, len(randomArr) - 1)
endTime = time.time()
totalTime = endTime - startTime

print("Sorted Array of 30,000 integers:", randomArr[:10], "...", randomArr[-10:])
print("Time for Merge Sort:", totalTime, "seconds")



