import random
import time
import csv
def InsertionSort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
    return array  

# Simple sorted array using insertion sort

Arr = [4, 2, 1, 5, 3]
sortedArr = InsertionSort(Arr)
print("Sorted Array is:", sortedArr)

# Saving Sorted array in sorted InsertionSelection csv file

sorted_filename = "SortedInsertionSort.csv"
with open(sorted_filename, 'w', newline='') as csvfile:
     writer = csv.writer(csvfile)
     for num in Arr:
      writer.writerow([num])

# Random array of 300000 integers sorted by this function

randomArr = [random.randint(1, 100000) for i in range(30000)]
sortedArr = InsertionSort(randomArr.copy())
print("Sorted Array of 30000 integers are:",sortedArr)

# Measuring Time
startTime = time.time()
sortedArr = InsertionSort(randomArr.copy())
endTime = time.time()
totalTime = endTime - startTime
print("Time for sorted arrays are:",totalTime,"Seconds")



  

  
            
    

