def min_sum_subarray(arr):
    if not arr:
        return 0, []
    min_sum = float('inf')
    current_sum = 0
    start = 0
    subarray = []
    min_start = 0
    for end, value in enumerate(arr):
        current_sum += value
        if current_sum < min_sum:
            min_sum = current_sum
            min_start = start
        if current_sum > 0:
            current_sum = 0
            start = end + 1
    subarray = arr[min_start:end + 1]
    return min_sum, subarray
arr = [3, -4, 2, -3, -1, 7, -5]
min_sum, subarray = min_sum_subarray(arr)
print("Sum of the contiguous subarray with the minimum sum:", min_sum)
print("Subarray with the minimum sum:", subarray)