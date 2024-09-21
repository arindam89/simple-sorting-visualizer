from flask import Flask, render_template, request, jsonify
from sorting import bubble_sort, quick_sort, merge_sort, heap_sort, radix_sort
from sorting.algorithm_info import algorithm_info
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', algorithms=algorithm_info)

@app.route('/sort', methods=['POST'])
def sort():
    data = request.json
    array = data['array']
    algorithm = data['algorithm']
    
    if algorithm == 'bubble':
        steps = bubble_sort(array)
    elif algorithm == 'quick':
        steps = quick_sort(array)
    elif algorithm == 'merge':
        steps = merge_sort(array)
    elif algorithm == 'heap':
        steps = heap_sort(array)
    elif algorithm == 'radix':
        steps = radix_sort(array)
    else:
        return jsonify({'error': 'Invalid algorithm'}), 400
    
    return jsonify({'steps': steps, 'info': algorithm_info[algorithm]})

@app.route('/compare', methods=['POST'])
def compare_algorithms():
    data = request.json
    array = data['array']
    algorithms = data['algorithms']
    
    results = {}
    
    for alg in algorithms:
        start_time = time.time()
        if alg == 'bubble':
            bubble_sort(array.copy())
        elif alg == 'quick':
            quick_sort(array.copy())
        elif alg == 'merge':
            merge_sort(array.copy())
        elif alg == 'heap':
            heap_sort(array.copy())
        elif alg == 'radix':
            radix_sort(array.copy())
        else:
            return jsonify({'error': f'Invalid algorithm: {alg}'}), 400
        
        end_time = time.time()
        execution_time = end_time - start_time
        results[alg] = {
            'execution_time': execution_time,
            'info': algorithm_info[alg]
        }
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
