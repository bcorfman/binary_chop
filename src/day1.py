def chop(target, sorted_arr):
    return _chop(target, sorted_arr, 0, len(sorted_arr))


def _chop(target, sorted_arr, start, end):
    slice_length = end - start
    idx = -1
    if slice_length == 1:
        idx = start if sorted_arr[start] == target else -1
    if slice_length > 1:
        mid = slice_length // 2 + start
        if target < sorted_arr[mid]:
            idx = _chop(target, sorted_arr, start, mid)
        else:
            idx = _chop(target, sorted_arr, mid, end)
    return idx