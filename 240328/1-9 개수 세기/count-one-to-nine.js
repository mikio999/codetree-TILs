const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split('\n')

const n = parseInt(input[0])

const numberList = input[1].split(' ').map(function(element){
    return Number(element)
})

let cntNumbers = Array(9).fill(0)

for (let i = 0; i < n; i++ ) {
    let index = numberList[i] - 1
    cntNumbers[index] += 1
}

for (let j = 0; j < cntNumbers.length; j++ ) {
    console.log(cntNumbers[j])
}