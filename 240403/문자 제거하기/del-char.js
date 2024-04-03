const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

let str = input[0]
let i = 1
while (i <= input.length - 1) {
    if (Number(input[i]) < str.length) {
        str = str.slice(0, Number(input[i])) + str.slice(Number(input[i])+1)
        console.log(str)
        i += 1
    }
    else {
        str = str.slice(0,-1)
        console.log(str)
        i += 1
    }
}