const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

let repeat = []

for (let i = 0; i < 8; i++) {
    repeat.push(input)
}

console.log(repeat.join(''))