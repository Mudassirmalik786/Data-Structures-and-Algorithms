import csv
#These functions are imported from funcs.py file which we created for functions
from funcs import RandomArray, InsertionSort, MergeSort, HybridMergeSort, BubbleSort, SelectionSort, measure_sorting_time

# Read the values of n from the file
n_values = []
#File open in append mode
with open('Nvalues.txt', 'r') as file:
    for line in file:
        n = int(line.strip())
        n_values.append(n)

# Open a CSV file to write the results
with open('RunTime.csv', 'w', newline='') as csvfile:
    columnnames = ['Value of n', 'Insertion sort (seconds)', 'Merge Sort (seconds)',
                  'Hybrid Merge Sort (seconds)', 'Selection Sort (seconds)', 'Bubble Sort (seconds)']
    writer = csv.DictWriter(csvfile, columnnames=columnnames)
    writer.writeheader()

    for n in n_values:
        array = RandomArray(n) # RamdomArray function written in funcs.py

        # Measure the sorting times for different algorithms
        insertion_sort_time = measure_sorting_time(InsertionSort, array.copy(), 0, n)
        merge_sort_time = measure_sorting_time(MergeSort, array.copy(), 0, n - 1)  
        hybrid_merge_sort_time = measure_sorting_time(HybridMergeSort, array.copy(), 0, n-1, n = 1)
        selection_sort_time = measure_sorting_time(SelectionSort, array.copy(), 0, n)
        bubble_sort_time = measure_sorting_time(BubbleSort, array.copy(), 0, n)

        # Write the results in the CSV(Comma Separated Value) file
        writer.writerow({
            'Value of n': n,
            'Insertion sort (seconds)': insertion_sort_time,
            'Merge Sort (seconds)': merge_sort_time,
            'Hybrid Merge Sort (seconds)': hybrid_merge_sort_time,
            'Selection Sort (seconds)': selection_sort_time,
            'Bubble Sort (seconds)': bubble_sort_time
        })
