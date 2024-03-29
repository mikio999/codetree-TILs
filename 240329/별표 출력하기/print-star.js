const fs = require('fs')
const input = fs.readFileSync(0).toString()
const n = parseInt(input)

let str = ''

for (let i = 0; i < 2 * n - 1; i ++ ){
    if (i < n) {
        str += '* '
        console.log(str)
    }
    else if (i == n-1) {
        str = '* '.repeat(n)
        console.log(str) 
    }
    else {
        str = '* '.repeat(2*n-i-1)
        console.log(str)
    }
}