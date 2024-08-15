const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const [n,m] = input[0].split(' ').map(Number)

const numbers = input[1].split(' ').map(Number)
const questions = input[2].split(' ').map(Number)

const frequencyMap = new Map();
for (let i = 0; i < n; i++) {
    const num = numbers[i];
    if (frequencyMap.has(num)) {
        frequencyMap.set(num, frequencyMap.get(num) + 1);
    } else {
        frequencyMap.set(num, 1);
    }
}

const result = [];
for (let j = 0; j < m; j++) {
    result.push(frequencyMap.get(questions[j]) || 0);
}

console.log(result.join(' '));