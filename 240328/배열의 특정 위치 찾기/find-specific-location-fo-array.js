const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(' ')

const numberList = input.map(function(element){
    return parseInt(element)
})

let evenInputSum = 0
let threeInputSum = 0
let threeCnt = 0

for (i=0; i<10; i++) {
    if ((i+1) % 2 == 0) {
        evenInputSum += numberList[i]
    }
    if ((i+1) % 3 == 0) {
        threeInputSum += numberList[i]
        threeCnt += 1
    }
}

let threeInputAverage = parseFloat(threeInputSum/threeCnt).toFixed(1)

let answer = String(evenInputSum) + ' ' + String(threeInputAverage)
console.log(answer)