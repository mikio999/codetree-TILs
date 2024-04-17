const fs = require('fs')
const numbers = fs.readFileSync(0).toString().trim().split(' ').map(Number)

let target = numbers[0] * numbers[1] * numbers[2]
let result = 0

function f(n) {
    if (n < 10) {
        result += n
        return result;
    }
    else {
        let a = n%10
        result += a
        return f(parseInt(n/10))
    }
}

console.log(f(target))