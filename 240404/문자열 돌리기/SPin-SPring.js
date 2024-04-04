const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()
const L = input.length
console.log(input)

let word = input

for (let i=0; i < L; i++) {
    word = word[L-1] + word.slice(0,L-1)
    console.log(word)
}