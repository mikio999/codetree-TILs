const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const word = input[0]
const n = input[1]
const lastIndex = word.length - 1
const firstIndex = lastIndex - n > 0 ? lastIndex - n : 0

let str = ''

if (lastIndex === firstIndex) {
    str = word
}
else {
    for (let i = lastIndex; i > firstIndex; i -- ) {
        str += (word[i])
}
}

console.log(str)