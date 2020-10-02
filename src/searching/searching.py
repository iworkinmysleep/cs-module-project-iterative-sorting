def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = (len(arr) - 1)
    mid = 0

    while start <= end:
        mid = (end + start) // 2
        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return mid


    return -1  # not found
