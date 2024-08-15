const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const [n,m] = input[0].split(' ').map(Number)

const numbers = input[1].split(' ').map(Number)
const questions = input[2].split(' ').map(Number)

const countNums = (arr, target) => {
  const k = new Map()
    for (let i=0; i < n; i++) {
        if (k.has(numbers[i])) {
            k.set(numbers[i], k.get(numbers[i]) + 1)
        }
        else {
            k.set(numbers[i], 1)
        }
    }
    return (k.get(target) || 0)
}



for (let j=0; j<m; j++) {
    console.log(countNums(numbers, questions[j]))
}