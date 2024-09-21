def merge_sort(arr):
    steps = []

    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            steps.append({'array': arr.copy(), 'comparing': [left[i], right[j]], 'swapping': []})
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort_helper(start, end):
        if end - start > 1:
            mid = (start + end) // 2
            merge_sort_helper(start, mid)
            merge_sort_helper(mid, end)
            merged = merge(arr[start:mid], arr[mid:end])
            arr[start:end] = merged
            steps.append({'array': arr.copy(), 'comparing': [], 'swapping': list(range(start, end))})

    merge_sort_helper(0, len(arr))
    steps.append({'array': arr.copy(), 'comparing': [], 'swapping': []})
    return steps
