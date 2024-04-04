const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
let A = input[0]
const command = input[1]

for (let i = 0; i < command.length; i++ ) {
    if (command[i] === 'L') {
        A = A.slice(1) + A[0]
    }
    else if (command[i] === 'R') {
        A = A[A.length - 1] + A.slice(0, -1)
    }
}

console.log(A)