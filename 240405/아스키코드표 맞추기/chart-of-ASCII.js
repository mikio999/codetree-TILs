const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(' ').map(Number)

let str = ''

for (let i = 0; i < 5; i++ ) {
    str += String.fromCharCode(input[i]) + ' '
}

console.log(str)