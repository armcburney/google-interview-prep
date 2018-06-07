def binary_search(arr, value):
    if len(arr) is 0:
        return False

    m = len(arr) // 2

    if arr[m] is value:
        return True
    elif value < arr[m]:
        return binary_search(arr[:m], value)
    else:
        return binary_search(arr[m + 1:], value)
