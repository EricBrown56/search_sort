def binary_search(arr, target):
    high = len(arr) -1
    low = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1

    return -1