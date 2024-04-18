const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const n = input[0]
let answer = []
for (let i = 1; i < n+1; i++) {
    answer.push(input[i])
}
answer.sort()

for (let j = 0; j < n; j++) {
    console.log(answer[j])
}