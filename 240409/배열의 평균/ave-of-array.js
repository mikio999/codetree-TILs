const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

let grid = []

for (let i = 0; i < 2; i++ ) {
    grid.push(input[i].split(' ').map(Number))
}

let answerFirst = []
for (let i = 0; i < 2; i ++ ) {
    let sum = 0
    for (let j = 0; j < 4; j ++ ) {
        sum += grid[i][j]
    }
    answerFirst.push((sum/4).toFixed(1))
}
console.log(answerFirst.join(' '))

let answerSecond = []
for (let i = 0; i < 4; i ++ ) {
    let sum = 0
    for (let j = 0; j < 2; j ++ ) {
        sum += grid[j][i]
    }
    answerSecond.push((sum/2).toFixed(1))
}

console.log(answerSecond.join(' '))

let answerThird = 0

for (let i=0; i<2; i++ ) {
    for (let j=0; j<4; j++) {
        answerThird += grid[i][j]
    }
}

console.log((answerThird/8).toFixed(1))