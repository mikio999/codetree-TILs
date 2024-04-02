const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

let str = input[0];
let a = input[1];

let len = str.length;
let cnt = 0;

let rev = '';
for (let i = len - 1; i >= 0; i--) {
    if(cnt >= a) break;
    rev += str[i]
    cnt += 1;
}

console.log(rev)