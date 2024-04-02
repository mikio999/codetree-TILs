const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const n = Number(input[0])
const numbers = input[1].split(' ')

let str = ''
for (i=0; i < n; i++ ) {
    for (j=0; j < numbers[i].length; j++) {
        str += numbers[i][j]
    }
}

for (let k = 0; k < str.length; k = k+5) {
    console.log(str.slice(k,k+5))
}