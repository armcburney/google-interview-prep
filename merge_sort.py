def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def merge(arr1, arr2):
    arr = []
    i, j = 0, 0

    for _ in range(len(arr1) + len(arr2)):
        if j >= len(arr2) or (i < len(arr1) and arr1[i] <= arr2[j]):
            i += 1
            arr.append(arr1[i - 1])
        elif j < len(arr2):
            j += 1
            arr.append(arr2[j - 1])

    return arr
