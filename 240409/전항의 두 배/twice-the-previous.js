const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(' ').map(Number)

let numbers = input

for (let i = 2; i < 10; i++) {
    numbers.push(numbers[i-1] + 2 * (numbers[i-2]))
}

console.log(numbers.join(' '))