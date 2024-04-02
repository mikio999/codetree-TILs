const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const word = input[0]
const n = input[1]
const start =  word.length > n ? word.length - n : 0
const reverseList = []

for (let i = start; i < word.length; i++) {
    reverseList.unshift(word[i])
}


let str = ''
for (let j = 0; j < reverseList.length; j++ ) {
    str += reverseList[j]
}

console.log(str)