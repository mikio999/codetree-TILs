const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()
let n = Number(input)

let isComposite = false

for (let i = 2; i <= n-1; i++) {
    if (n%i == 0) {
        isComposite = true
    }
}

console.log(isComposite ? 'C' : 'N')