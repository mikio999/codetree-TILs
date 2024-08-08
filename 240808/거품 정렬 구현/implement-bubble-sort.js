const fs = require('fs');
let a = fs.readFileSync(0).toString().trim().split(`\n`)
let numbers = a[1].split(' ').map(Number)

function bubbleSort(arr) {
    let n = arr.length;
    let swapped;
    do {
        swapped = false;
        for (let i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                let temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
                swapped = true;
            }
        }
        n--;
    } while (swapped);
    return arr;
}

console.log(bubbleSort(numbers).join(' '))