const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const request = input[0].split(' ')
let target = request[0]
const q = parseInt(request[1])

for (let i = 1; i < q+1; i++ ) {
    if (input[i] === '1') {
        target = target.slice(1) + target[0]
        console.log(target)
    }
    else if (input[i] === '2') {
        target = target.slice(-1) + target.slice(0, -1)
        console.log(target)
    }
    else if (input[i] === '3') {
        target = target.split('').reverse().join('')
        console.log(target)
    }
}