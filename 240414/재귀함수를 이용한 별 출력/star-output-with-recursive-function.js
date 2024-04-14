const fs = require('fs')
const N = Number(fs.readFileSync(0).toString().trim())


function f(n) {
    if (n === 0) {
        return;
    }
    f(n-1)
    for (let i = 0; i < n; i++) {
        process.stdout.write('*')
    }
    console.log();
}

f(N)