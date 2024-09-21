def quick_sort(arr):
    steps = []
    
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            steps.append({'array': arr.copy(), 'comparing': [j, high], 'swapping': []})
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                steps.append({'array': arr.copy(), 'comparing': [j, high], 'swapping': [i, j]})
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps.append({'array': arr.copy(), 'comparing': [], 'swapping': [i + 1, high]})
        return i + 1

    def quick_sort_helper(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_helper(low, pi - 1)
            quick_sort_helper(pi + 1, high)

    quick_sort_helper(0, len(arr) - 1)
    steps.append({'array': arr.copy(), 'comparing': [], 'swapping': []})
    return steps
