const fs = require('fs')
const N = Number(fs.readFileSync(0).toString().trim())

function f(n) {
    if (n === 1) {
        return 2;
    }
    if (n === 2) {
        return 4;
    }
    else {
        return (f(n-1) * f(n-2)) % 100;
    }
}

console.log(f(N))