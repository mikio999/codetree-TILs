const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

let i = 0
let str = ''
let cnt = 0
while (i < input.length) {
    if (input[i] === input[i+1]) {
        cnt += 1
        i = i+1
    }
    else {
        cnt += 1
        str += input[i]
        str += String(cnt)
        i += 1
        cnt = 0
    }
}

console.log(str.length)
console.log(str)