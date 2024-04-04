const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(' ')
const A = Number(input[0])
const B = Number(input[1])

const target = (A+B).toString()
let cnt = 0

for (let i = 0; i< target.length; i++ ) {
    if (target[i] === '1') {
        cnt += 1
    }
}

console.log(cnt)