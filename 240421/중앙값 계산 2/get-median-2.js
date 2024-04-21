const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const N = Number(input[0])
const numbers = input[1].split(' ').map(Number)

let numList = []
let answer = ''
for (let i = 0; i < N; i++) {
    numList.push(numbers[i])
    if (i % 2 === 0) {
        numList.sort((a,b) => a-b)
        answer += (numList[parseInt((numList.length)/2)]) + ' '
    }
}
console.log(answer)