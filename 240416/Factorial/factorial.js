const fs = require('fs')
const N = Number(fs.readFileSync(0).toString().trim())

function f(n) {
    if (n === 1) {
        return 1;
    }
    else {
        return f(n-1) * n;
    }
}

console.log(f(N))