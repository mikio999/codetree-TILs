const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const n = Number(input[0])
const numbers = input[1].split(' ').map(Number)
const k = n - 1
let maxNumber = numbers[0]

function f(x) {
    if (x === 0) {
        return maxNumber
    }
    else {
        if (maxNumber < numbers[x]) {
            maxNumber = numbers[x]
        }
        return f(x-1);
    }
}

console.log(f(k))