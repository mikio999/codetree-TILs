const fs = require('fs')
const N = Number(fs.readFileSync(0).toString().trim())

let firstLine = ''
let secondLine = ''
function printNumbers(n) {
    if (n === 0) {
        return;
    }
    printNumbers(n-1);
    firstLine += n + ' '
}
printNumbers(N)
console.log(firstLine)

function reverseNumbers(n) {
    if (n === 0) {
        return;
    }
    secondLine += n + ' '
    reverseNumbers(n-1)
}

reverseNumbers(N)
console.log(secondLine)