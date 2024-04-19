const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);
const a = input[1].split(' ').map(Number);
const b = input[2].split(' ').map(Number);


const equal = () => {
     for (let i = 0; i < n; i++) {
        if (a[i] !== b[i]) {
            return false;
        }
    }
    return true;
}

a.sort((a,b) => a-b);
b.sort((a,b) => a-b);

if (equal()) {
    console.log("Yes");
} else {
    console.log("No");
}