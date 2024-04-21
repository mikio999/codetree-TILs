const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const first = input[0].split(' ')

const n = Number(first[0])
const k = Number(first[1])
const T = first[2]

let TList = []

for (let i = 1; i < n; i++ ) {
    if (T === input[i].slice(0,2)) {
        TList.push(input[i])
    }
}

TList.sort()

console.log(TList[k-1])