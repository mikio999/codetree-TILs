const fs = require('fs')
const input= fs.readFileSync(0).toString().split(`\n`)

for (let i = 0; i < 4; i ++) {
    numbers = input[i].split(' ').map(Number)
    let sumVal = 0
    for (let j = 0; j < 4; j++) {
        sumVal += numbers[j]
    }
    console.log(sumVal)
}