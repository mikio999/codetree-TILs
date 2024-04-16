const fs = require('fs')
const N = Number(fs.readFileSync(0).toString().trim())

let count = 0;
function f(n) {
    if (n === 1) {
        return count;
    } 
    else {
        if (n%2 === 0) {
            count += 1;
            return f(n/2);
        }
        else {
            count += 1;
            return f(parseInt(n/3));
        }
    }
}

console.log(f(N));