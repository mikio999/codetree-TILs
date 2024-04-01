const fs = require('fs')
const inputs = fs.readFileSync(0).toString().trim().split(`\n`)
const input = inputs[0] + inputs[1]

let str = ''

for (let i = 0; i < input.length; i ++ ) {
    if (input[i] == ' ') {
        continue;
    }
    else {
        str += input[i]
    }
}

console.log(str)