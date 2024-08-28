from merge import merged

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[0:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        merged(arr, left_half, right_half) 

    return -1

        
        
        





    