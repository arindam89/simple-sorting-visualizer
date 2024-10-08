document.addEventListener('DOMContentLoaded', () => {
    const arrayInput = document.getElementById('arrayInput');
    const arraySizeInput = document.getElementById('arraySizeInput');
    const minValueInput = document.getElementById('minValueInput');
    const maxValueInput = document.getElementById('maxValueInput');
    const generateBtn = document.getElementById('generateBtn');
    const sortBtn = document.getElementById('sortBtn');
    const algorithmSelect = document.getElementById('algorithmSelect');
    const speedInput = document.getElementById('speedInput');
    const canvas = document.getElementById('sortingCanvas');
    const ctx = canvas.getContext('2d');
    const algorithmInfo = document.getElementById('algorithmInfo');
    const compareBtn = document.getElementById('compareBtn');
    const comparisonResults = document.getElementById('comparisonResults');
    const explanationDiv = document.getElementById('explanation');

    let currentArray = [];
    let sortingSteps = [];
    let currentStep = 0;
    let animationId;

    const visualizer = new Visualizer(canvas, ctx);

    generateBtn.addEventListener('click', () => {
        const size = parseInt(arraySizeInput.value);
        const minValue = parseInt(minValueInput.value);
        const maxValue = parseInt(maxValueInput.value);
        
        if (size < 5 || size > 100 || minValue >= maxValue) {
            alert('Please enter valid array size (5-100) and value range.');
            return;
        }

        currentArray = Array.from({length: size}, () => Math.floor(Math.random() * (maxValue - minValue + 1)) + minValue);
        arrayInput.value = currentArray.join(', ');
        visualizer.drawArray(currentArray);
        explanationDiv.textContent = '';
    });

    sortBtn.addEventListener('click', async () => {
        const inputArray = arrayInput.value.split(',').map(num => parseInt(num.trim()));
        const algorithm = algorithmSelect.value;

        const response = await fetch('/sort', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({array: inputArray, algorithm: algorithm}),
        });

        const data = await response.json();
        sortingSteps = data.steps;
        currentStep = 0;
        cancelAnimationFrame(animationId);
        animate();
        displayAlgorithmInfo(data.info);
    });

    compareBtn.addEventListener('click', async () => {
        const inputArray = arrayInput.value.split(',').map(num => parseInt(num.trim()));
        const algorithms = Array.from(algorithmSelect.options).map(option => option.value);

        const response = await fetch('/compare', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({array: inputArray, algorithms: algorithms}),
        });

        const data = await response.json();
        displayComparisonResults(data);
    });

    function animate() {
        if (currentStep < sortingSteps.length) {
            const step = sortingSteps[currentStep];
            visualizer.drawArray(step.array, step.comparing || [], step.swapping || []);
            explanationDiv.textContent = step.explanation;
            currentStep++;
            const speed = 101 - speedInput.value;
            animationId = setTimeout(() => requestAnimationFrame(animate), speed);
        }
    }

    function displayAlgorithmInfo(info) {
        algorithmInfo.innerHTML = `
            <h2 class="text-2xl font-bold mb-2 text-blue-600">${info.name}</h2>
            <p class="mb-2"><strong class="text-gray-700">Time Complexity:</strong></p>
            <ul class="list-disc list-inside mb-2 text-gray-600">
                <li>Best: ${info.time_complexity.best}</li>
                <li>Average: ${info.time_complexity.average}</li>
                <li>Worst: ${info.time_complexity.worst}</li>
            </ul>
            <p class="mb-2"><strong class="text-gray-700">Space Complexity:</strong> <span class="text-gray-600">${info.space_complexity}</span></p>
            <p class="mb-2"><strong class="text-gray-700">Description:</strong> <span class="text-gray-600">${info.description}</span></p>
        `;
    }

    function displayComparisonResults(results) {
        let html = '<table class="w-full text-left border-collapse">';
        html += '<thead><tr class="bg-blue-100"><th class="p-2 border">Algorithm</th><th class="p-2 border">Execution Time (s)</th></tr></thead><tbody>';
        
        for (const [alg, data] of Object.entries(results)) {
            html += `<tr class="hover:bg-gray-100">
                <td class="p-2 border">${data.info.name}</td>
                <td class="p-2 border">${data.execution_time.toFixed(6)}</td>
            </tr>`;
        }
        
        html += '</tbody></table>';
        comparisonResults.innerHTML = html;
    }
});
