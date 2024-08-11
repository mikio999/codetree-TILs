const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const n = input[0]
let arr = input[1].split(' ').map(Number)

for (let i = 0; i < n-1; i++) {
    let min = i;
    for (let j = i+1; j < n; j++) {
        if (arr[j] < arr[min]) {
            min = j
        }
    }
    let tmp = arr[i]
    arr[i] = arr[min]
    arr[min] = tmp
}

console.log(arr.join(' '))