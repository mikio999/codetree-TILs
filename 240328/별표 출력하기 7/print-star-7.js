const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()
const n = parseInt(input)

for (let i = 1; i < n+1; i++ ) {
    str = ''
    str += '* '.repeat(i)
    console.log(str)
}