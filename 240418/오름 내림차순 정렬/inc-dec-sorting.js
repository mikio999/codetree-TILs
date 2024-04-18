const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const n = Number(input[0])
const numbers = input[1].split(' ').map(Number)


numbers.sort((a,b) => a - b)

console.log(numbers.join(' '))
numbers.reverse()
console.log(numbers.join(' '))