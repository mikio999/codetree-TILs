const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const n = input[0].split(' ').map(Number)[0];
const t = input[0].split(' ').map(Number)[1];

const numbers = input[1].split(' ').map(Number)

let maxVal = 0;
let repeatNumbers = 0;

for (let i = 0; i < n; i++ ) {
    if (numbers[i] > t) {
        repeatNumbers += 1
        maxVal = Math.max(maxVal, repeatNumbers)
    }
    else {
        repeatNumbers = 0
    }
}

console.log(maxVal)