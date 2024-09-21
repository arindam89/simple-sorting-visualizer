def bubble_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            steps.append({
                'array': arr.copy(),
                'comparing': [j, j + 1],
                'swapping': [],
                'explanation': f"Comparing elements at index {j} and {j+1}"
            })
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append({
                    'array': arr.copy(),
                    'comparing': [j, j + 1],
                    'swapping': [j, j + 1],
                    'explanation': f"Swapping elements at index {j} and {j+1}"
                })
    steps.append({
        'array': arr.copy(),
        'comparing': [],
        'swapping': [],
        'explanation': "Sorting complete"
    })
    return steps
