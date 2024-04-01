const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const target = input[10]
const answer = []
for (let i = 0; i < 10; i++ ) {
    let strLength = input[i].length
    if (input[i][strLength-1] === target) {
        console.log(input[i])
    }
}