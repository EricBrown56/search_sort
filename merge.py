def merge(list1, list2):

    one = 0
    two = 0
    merge = []

    while one < len(list1) and two < len(list2):
        if list1[one] < list2[two]:
            merge.append(list1[one])
            one += 1

        else:
            merge.append(list2[two])
            two += 1

    if one == len(list1):
        merge = merge + list2[two:]
    else:
        merge = merge + list1[one:]

    return merge

def merged(arr, left_half, right_half):
    l = 0
    r = 0
    a = 0

    while l < len(left_half) and r < len(right_half):
        if left_half[l].lower() < right_half[r].lower():
            arr[a] = left_half[l]
            l += 1
            a += 1
        else:
            arr[a] = right_half[r]
            r += 1
            a += 1

    while l < len(left_half):
        arr[a] = left_half[l]
        l += 1
        a += 1

    while r < len(right_half):
        arr[a] = right_half[r]
        r += 1
        a += 1
