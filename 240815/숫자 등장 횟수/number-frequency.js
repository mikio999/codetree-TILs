const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const [n,m] = input[0].split(' ').map(Number)

const numbers = input[1].split(' ').map(Number)
const questions = input[2].split(' ').map(Number)

const countNums = (arr, target) => {
  const k = new Map()
    for (let i=0; i < n; i++) {
        if (k.has(arr[i])) {
            k.set(arr[i], k.get(arr[i]) + 1)
        }
        else {
            k.set(arr[i], 1)
        }
    }
    return (k.get(target) || 0)
}


result = []
for (let j=0; j<m; j++) {
    result.push(countNums(numbers, questions[j]))
}
console.log(result.join(' '))