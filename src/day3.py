def _chop(tgt, lst, start, end):
    result = -1
    mid = start + (end - start) // 2
    if tgt == lst[start]:
        result = start 
    elif mid - start == 0:
        result = -1
    elif tgt < lst[mid]:
        result = _chop(tgt, lst, start, mid)
    else:
        result = _chop(tgt, lst, mid, end)
    return result

def chop(tgt, lst):
    return _chop(tgt, lst, 0, len(lst)) if lst else -1
