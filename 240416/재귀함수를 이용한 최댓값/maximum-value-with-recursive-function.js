const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const n = Number(input[0])
const numbers = input[1].split(' ').map(Number)


function f(x) {
    if (x === 0) return numbers[0];
    return Math.max(f(x-1), numbers[x])
}

console.log(f(n-1))