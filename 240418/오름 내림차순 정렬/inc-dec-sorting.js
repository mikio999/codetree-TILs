const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const n = Number(input[0])
const numbers = input[1].split(' ').map(Number)

function cmp(prev, cur) {
    return prev - cur;
}

numbers.sort(cmp)

let str1 = ''
for (let i = 0; i < n; i++) {
    str1 += numbers[i] + ' '
}
numbers.reverse()
let str2 = ''
for (let i = 0; i < n; i++) {
    str2 += numbers[i] + ' '
}


console.log(str1)
console.log(str2)