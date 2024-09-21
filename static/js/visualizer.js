class Visualizer {
    constructor(canvas, ctx) {
        this.canvas = canvas;
        this.ctx = ctx;
        this.barWidth = 20;
        this.barSpacing = 5;
    }

    drawArray(array, comparing = [], swapping = []) {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        const maxValue = Math.max(...array);

        array.forEach((value, index) => {
            const x = index * (this.barWidth + this.barSpacing);
            const height = (value / maxValue) * this.canvas.height;
            const y = this.canvas.height - height;

            if (swapping.includes(index)) {
                this.ctx.fillStyle = '#FF0000'; // Red for swapping
            } else if (comparing.includes(index)) {
                this.ctx.fillStyle = '#FFFF00'; // Yellow for comparing
            } else {
                this.ctx.fillStyle = '#4CAF50'; // Green for normal
            }

            this.ctx.fillRect(x, y, this.barWidth, height);
            this.ctx.strokeRect(x, y, this.barWidth, height);

            this.ctx.fillStyle = '#000000';
            this.ctx.fillText(value.toString(), x + this.barWidth / 2, this.canvas.height - 5);
        });
    }
}
