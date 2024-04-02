const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const word = input[0]
const target = input[1]
const targetLength = target.length

let index = 0
let isExist = false

while (!isExist) {
    if (word.slice(index, index+targetLength) == target) {
        isExist = true
        break;
    }
    else {
        if (index == word.length) {
            break;
        }
        else {
            index += 1
        }
    }
}

console.log(isExist ? index : -1 )