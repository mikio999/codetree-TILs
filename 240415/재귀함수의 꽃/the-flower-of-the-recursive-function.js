const fs = require('fs')
const N = Number(fs.readFileSync(0).toString().trim())

function f(n) {
    if (n === 0) {
        return;
    }
    process.stdout.write(`${n} `)
    f(n-1)
    process.stdout.write(`${n} `)
}

f(N)