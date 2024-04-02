const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

let index = 0
let cnt = 0
let answerList = []

while (input[index] != 0) {
    cnt += 1
    if (index%2 === 0) {
        answerList.push(input[index])
        index += 1
    }
    else {
        index += 1
    }
}

console.log(cnt)
for (let i = 0; i < answerList.length; i ++) {
    console.log(answerList[i])
}