const fs = require('fs')
const N = Number(fs.readFileSync(0).toString().trim())

function printNumbers(n) {
    if (n === 0) {
        return;
    }
    printNumbers(n-1);
    process.stdout.write(n + ' ');
}
printNumbers(N)

function reverseNumbers(n) {
    if (n === 0) {
        return;
    }
    process.stdout.write(n + ' ')
    reverseNumbers(n-1)
}
console.log();
reverseNumbers(N)