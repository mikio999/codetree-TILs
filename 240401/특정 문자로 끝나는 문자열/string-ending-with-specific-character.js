const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const target = input[10]
const answer = []
for (let i = 0; i < 10; i++ ) {
    let strLength = input[i].length
    if (input[i][strLength-1] === target) {
        answer.push(input[i])
        console.log(input[i])
    }
}

if (answer.length === 0) {
   console.log('None')
}