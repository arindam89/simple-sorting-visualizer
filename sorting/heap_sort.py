def heapify(arr, n, i, steps):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        steps.append({'array': arr.copy(), 'comparing': [i, largest], 'swapping': [i, largest]})
        heapify(arr, n, largest, steps)

def heap_sort(arr):
    steps = []
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, steps)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        steps.append({'array': arr.copy(), 'comparing': [0, i], 'swapping': [0, i]})
        heapify(arr, i, 0, steps)

    steps.append({'array': arr.copy(), 'comparing': [], 'swapping': []})
    return steps
