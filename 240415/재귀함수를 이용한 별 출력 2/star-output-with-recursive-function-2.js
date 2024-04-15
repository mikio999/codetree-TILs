const fs = require('fs')
const n = Number(fs.readFileSync(0).toString().trim())

function f(x) {
    if (x === 0) {
        return;
    }
    let stars = '* '.repeat(x)
    process.stdout.write(`${stars}`)
    process.stdout.write(`\n`)
    f(x-1)
    process.stdout.write(`${stars}`)
    process.stdout.write(`\n`)
}

f(n)