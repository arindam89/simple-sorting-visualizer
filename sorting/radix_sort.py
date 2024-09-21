def counting_sort(arr, exp, steps):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        if arr[i] != output[i]:
            arr[i] = output[i]
            steps.append({'array': arr.copy(), 'comparing': [i], 'swapping': [i]})

def radix_sort(arr):
    steps = []
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort(arr, exp, steps)
        exp *= 10

    steps.append({'array': arr.copy(), 'comparing': [], 'swapping': []})
    return steps
