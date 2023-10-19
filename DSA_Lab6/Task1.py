def counting_sort(input_array):
    # Find the minimum and maximum values in the input array
    min_val = min(input_array)
    max_val = max(input_array)
    
    # Adjust the range of elements to be non-negative
    adjusted_array = [x - min_val for x in input_array]
    k = max_val - min_val + 1

    # Initialize count and output arrays
    count = [0] * k
    output = [0] * len(adjusted_array)

    # Count the occurrences of each element
    for i in range(len(adjusted_array)):
        count[adjusted_array[i]] += 1

    # Update count to store the position of the last occurrence of each element
    for i in range(1, k):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(len(adjusted_array) - 1, -1, -1):
        output[count[adjusted_array[i]] - 1] = adjusted_array[i]
        count[adjusted_array[i]] -= 1

    # Adjust the output array to revert the value shifting
    sorted_array = [x + min_val for x in output]

    return sorted_array

# Example usage
input_array = [4, -2, 2, -8, 3, 3, -1, 4, 5, 0]
sorted_array = counting_sort(input_array)
print(sorted_array)
