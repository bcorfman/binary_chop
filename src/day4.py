def chop(tgt, lst):
    def _binary_search(start_idx, end_idx):
        result = -1
        mid_idx = start_idx + (end_idx - start_idx) // 2
        if tgt == lst[start_idx]:
            result = start_idx 
        elif mid_idx - start_idx == 0:
            result = -1
        elif tgt < lst[mid_idx]:
            result = _binary_search(start_idx, mid_idx)
        else:
            result = _binary_search(mid_idx, end_idx)
        return result

    return _binary_search(0, len(lst)) if lst else -1
