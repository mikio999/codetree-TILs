const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const target = input[0]
const alphabet = input[1]
let cnt = 0

for (let i = 0; i < target.length; i++ ) {
    if (target[i] == alphabet) {
        cnt += 1
    }
}

console.log(cnt)