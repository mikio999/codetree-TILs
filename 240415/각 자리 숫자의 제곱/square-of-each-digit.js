const fs = require('fs')
const N = Number(fs.readFileSync(0).toString().trim())

function f(n) {
    if (n < 10) {
        return n ** 2
    }
    let digit = (n % 10) ; 
    return f(parseInt(n/10)) + digit ** 2
}

console.log(f(N))