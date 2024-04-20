const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const N = Number(input[0])
const numbers = input[1].split(' ').map(Number)

numbers.sort((a,b) => a-b)

let groups = []

for (let i = 0; i < N; i++) {
    groups.push([])
}


for (let i = 0; i < N; i ++) {
    groups[i].push(numbers[i]);
    groups[i].push(numbers[2*N - i -1])
}


let maxSum = 0

for (let j = 0; j < N; j++) {
    if (maxSum < groups[j][0] + groups[j][1]) {
        maxSum = groups[j][0] + groups[j][1]
    }
}

console.log(maxSum)