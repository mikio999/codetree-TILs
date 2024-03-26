const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
let n;
let index = 0;

while (true) {
    n = Number(input[index])
    if (n == 0) {
        break
    }
    console.log(input[index])
    index += 1
}