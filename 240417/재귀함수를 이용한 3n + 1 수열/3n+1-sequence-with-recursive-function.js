const fs = require('fs')
const n = Number(fs.readFileSync(0).toString().trim())

let count = 0;

function f(n) {
    if (n===1) {
        return count;
    }
    else {
        if (n%2 === 0) {
            count ++
            return f(n/2)
        }
        else {
            count ++
            return f(3*n + 1)
        }
    }
}

console.log(f(n))