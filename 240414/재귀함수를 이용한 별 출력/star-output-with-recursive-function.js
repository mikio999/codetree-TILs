const fs = require('fs')
const N = Number(fs.readFileSync(0).toString().trim())

let stars = ''
function f(n) {
    if (n === 0) {
        return;
    }
    stars += '*' 
    console.log(stars)
    f(n-1)
}

f(N)