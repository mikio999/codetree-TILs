const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const n = input[0];
const arr = input[1].split(' ').map(Number);

const getDigit = (num, target) => {
    return Math.floor(Math.abs(num)/(Math.pow(10,target)))%10
}

const radixSort = (n,arr) => {
    for (let k = 0; k < n; k++) {
        let digitBuckets = Array.from({length:10}, () => []);
        for (let i=0; i<arr.length;i++) {
            let digit = getDigit(arr[i], k);
            digitBuckets[digit].push(arr[i])
        }
        arr = [].concat(...digitBuckets)
    }
    return arr
}

console.log(radixSort(n,arr).join(' '))