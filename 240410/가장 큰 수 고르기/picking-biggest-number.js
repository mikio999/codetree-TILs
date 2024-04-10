const fs = require('fs')
const input =fs.readFileSync(0).toString().trim().split(' ').map(Number)

let maxVal = input[0]

for (let i=0; i < 10; i++) {
    if (input[i] > maxVal) {
        maxVal = input[i];
    }
}

console.log(maxVal)