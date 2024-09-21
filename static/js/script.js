document.addEventListener('DOMContentLoaded', () => {
    const arrayInput = document.getElementById('arrayInput');
    const generateBtn = document.getElementById('generateBtn');
    const sortBtn = document.getElementById('sortBtn');
    const algorithmSelect = document.getElementById('algorithmSelect');
    const speedInput = document.getElementById('speedInput');
    const canvas = document.getElementById('sortingCanvas');
    const ctx = canvas.getContext('2d');

    let currentArray = [];
    let sortingSteps = [];
    let currentStep = 0;
    let animationId;

    const visualizer = new Visualizer(canvas, ctx);

    generateBtn.addEventListener('click', () => {
        const size = 20;
        currentArray = Array.from({length: size}, () => Math.floor(Math.random() * 100) + 1);
        arrayInput.value = currentArray.join(', ');
        visualizer.drawArray(currentArray);
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
    });

    function animate() {
        if (currentStep < sortingSteps.length) {
            visualizer.drawArray(sortingSteps[currentStep], sortingSteps[currentStep].comparing, sortingSteps[currentStep].swapping);
            currentStep++;
            const speed = 101 - speedInput.value;
            animationId = setTimeout(() => requestAnimationFrame(animate), speed);
        }
    }
});
