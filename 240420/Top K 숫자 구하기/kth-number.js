const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const N = Number(input[0].split(' ')[0])
const k = Number(input[0].split(' ')[1])

const numbers = input[1].split(' ').map(Number)

numbers.sort((a,b) => a-b)

console.log(numbers[k-1])