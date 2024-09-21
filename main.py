from flask import Flask, render_template, request, jsonify
from sorting import bubble_sort, quick_sort, merge_sort, heap_sort, radix_sort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
    
    return jsonify({'steps': steps})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
