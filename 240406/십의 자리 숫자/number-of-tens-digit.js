const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(' ').map(Number)

const numbers = []
let cnt = [0,0,0,0,0,0,0,0,0]

let index = 0;

while (input[index] !== 0) {
    if (input[index] >= 10) {
        numbers.push(input[index])
    }
    index += 1
}

for (let i = 0; i < numbers.length; i++ ) {
    let target = parseInt(numbers[i]/10) - 1
    cnt[target] += 1
}


for (let j=0; j<9; j++) {
    console.log(`${j+1} - ${cnt[j]}`)
}