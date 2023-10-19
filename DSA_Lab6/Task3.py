def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key


def bucket_sort(arr):
    # Create buckets
    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]

    # Plce numbrs into buckts basd on their fractional prt
    for num in arr:
        bucket_index = int(num * num_buckets)
        buckets[bucket_index].append(num)

    for i in range(num_buckets):
        insertion_sort(buckets[i])

    # Concatnate sorted buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

#main progrm
arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
sorted_arr = bucket_sort(arr)
print("Original array:", arr)
print("Sorted array:", sorted_arr)
