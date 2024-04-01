const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const target = input[10]
const cnt = 0
for (let i = 0; i < 10; i++ ) {
    let strLength = input[i].length
    if (input[i][strLength-1] === target) {
        cnt++;
        console.log(input[i])
    }
}

if (cnt === 0) {
   console.log('None')
}