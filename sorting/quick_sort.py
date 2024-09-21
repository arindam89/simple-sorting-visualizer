def quick_sort(arr):
    steps = []
    
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        steps.append({
            'array': arr.copy(),
            'comparing': [],
            'swapping': [],
            'explanation': f"Choosing pivot element: {pivot} at index {high}"
        })
        for j in range(low, high):
            steps.append({
                'array': arr.copy(),
                'comparing': [j, high],
                'swapping': [],
                'explanation': f"Comparing element {arr[j]} at index {j} with pivot {pivot}"
            })
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                steps.append({
                    'array': arr.copy(),
                    'comparing': [j, high],
                    'swapping': [i, j],
                    'explanation': f"Swapping elements at index {i} and {j}"
                })
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps.append({
            'array': arr.copy(),
            'comparing': [],
            'swapping': [i + 1, high],
            'explanation': f"Placing pivot {pivot} at its correct position (index {i+1})"
        })
        return i + 1

    def quick_sort_helper(low, high):
        if low < high:
            pi = partition(low, high)
            steps.append({
                'array': arr.copy(),
                'comparing': [],
                'swapping': [],
                'explanation': f"Recursively sorting left subarray (index {low} to {pi-1})"
            })
            quick_sort_helper(low, pi - 1)
            steps.append({
                'array': arr.copy(),
                'comparing': [],
                'swapping': [],
                'explanation': f"Recursively sorting right subarray (index {pi+1} to {high})"
            })
            quick_sort_helper(pi + 1, high)

    quick_sort_helper(0, len(arr) - 1)
    steps.append({
        'array': arr.copy(),
        'comparing': [],
        'swapping': [],
        'explanation': "Sorting complete"
    })
    return steps
