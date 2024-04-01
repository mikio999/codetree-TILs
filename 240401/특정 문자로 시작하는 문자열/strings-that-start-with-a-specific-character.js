const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const n = parseInt(input[0])
const target = input[n+1]
let targetList = []

for (i=1; i<n+1; i++) {
    if (input[i][0] === target) {
        targetList.push(input[i])
    }
}

let average = 0
let cnt = 0
let total = 0

for (j=0; j < targetList.length; j ++ ) {
    cnt += 1
    total += targetList[j].length
    average = (total/cnt).toFixed(2)
}

console.log(cnt, average)