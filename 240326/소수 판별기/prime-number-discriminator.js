const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()
let n = Number(input)

let isPrime = true

for (let i=2; i < n; i++) {
    if (n%i==0){
        isPrime = false
    }
}

console.log(isPrime ? 'P' : 'C')