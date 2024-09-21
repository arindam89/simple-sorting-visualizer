algorithm_info = {
    'bubble': {
        'name': 'Bubble Sort',
        'time_complexity': {
            'best': 'O(n)',
            'average': 'O(n^2)',
            'worst': 'O(n^2)'
        },
        'space_complexity': 'O(1)',
        'description': 'A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.'
    },
    'quick': {
        'name': 'Quick Sort',
        'time_complexity': {
            'best': 'O(n log n)',
            'average': 'O(n log n)',
            'worst': 'O(n^2)'
        },
        'space_complexity': 'O(log n)',
        'description': 'An efficient, recursive divide-and-conquer approach to sorting an array. It works by selecting a "pivot" element and partitioning the other elements into two sub-arrays.'
    },
    'merge': {
        'name': 'Merge Sort',
        'time_complexity': {
            'best': 'O(n log n)',
            'average': 'O(n log n)',
            'worst': 'O(n log n)'
        },
        'space_complexity': 'O(n)',
        'description': 'A divide-and-conquer algorithm that divides the input array into two halves, recursively sorts them, and then merges the two sorted halves.'
    },
    'heap': {
        'name': 'Heap Sort',
        'time_complexity': {
            'best': 'O(n log n)',
            'average': 'O(n log n)',
            'worst': 'O(n log n)'
        },
        'space_complexity': 'O(1)',
        'description': 'A comparison-based sorting algorithm that uses a binary heap data structure. It divides the input into a sorted and an unsorted region, and iteratively shrinks the unsorted region by extracting the largest element.'
    },
    'radix': {
        'name': 'Radix Sort',
        'time_complexity': {
            'best': 'O(nk)',
            'average': 'O(nk)',
            'worst': 'O(nk)'
        },
        'space_complexity': 'O(n + k)',
        'description': 'A non-comparative sorting algorithm that sorts integers by processing each digit position. It sorts the elements by grouping keys by the individual digits which share the same significant position and value.'
    }
}
