const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const [n,m] = input[0].split(' ').map(Number)

const numbers = input[1].split(' ').map(Number)
const questions = input[2].split(' ').map(Number)

const k = new Map()
for (let i=0; i < n; i++) {
    k.set(numbers[i], i+1);
}

let result = []
for (let j=0; j < m; j++) {
    let target = questions[j];
    let tmp = 0
    for (let i=0; i<n; i++) {
        if (target === numbers[i]) {
            tmp += 1;
        }
    }
   result.push(tmp)
}

console.log(result.join(' '))