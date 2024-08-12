const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`);
const n = input[0]
const arr = input[1].split(' ').map(Number)

for (let i = 1; i < n; i++ ) {
    let key = arr[i];
    j = i - 1;
    while (j >= 0 && arr[j] > key) {
        arr[j+1] = arr[j]
        arr[j] = key;
        j--;
    }
    arr[j+1] = key;
}

console.log(arr.join(' '))