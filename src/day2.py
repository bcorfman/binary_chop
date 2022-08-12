
def chop(target, arr, start=0):
    result = -1
    length = len(arr)
    if length:
        while length - start > 1:
            mid = start + (length - start) // 2
            if target >= arr[mid]:
                start = mid
            else:
                length = mid
        if target == arr[start]:
            result = start
    return result
