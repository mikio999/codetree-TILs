const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(' ')

const a = Number(input[0])
const b = Number(input[1])

let evenNumbers = []

for (i=a; i<=b; i++) {
    if (i%2==0) {
        evenNumbers.push(i)
    }
}

for (j=1; j<=9; j++) {
    let row = []
    for (i=evenNumbers.length - 1; i >= 0 ; i--) {
        row.push(`${evenNumbers[i]} * ${j} = ${evenNumbers[i]*j}`)
        //  console.log(`${evenNumbers[i]} * ${j} = ${evenNumbers[i]*j}`)
    }
    console.log(row.join(' / '))
}