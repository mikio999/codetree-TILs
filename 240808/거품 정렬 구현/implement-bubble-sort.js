const fs = require('fs');
let a = fs.readFileSync(0).toString().split(`\n`)
let n = parseInt(a[0]);
let numbers = a[1].split(' ').map(Number)

let isSorted = true;

do {
    isSorted = true;
    let temp
    for (let i = 0; i < n-1; i++) {
        if (numbers[i] > numbers[i+1]) {
            temp = numbers[i];
            numbers[i] = numbers[i+1];
            numbers[i+1] = temp;
            isSorted = false
        }
    }
} while (isSorted === false)

console.log(numbers.join(' '))