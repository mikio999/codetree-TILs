const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const n = parseInt(input[0], 10);
const arr = input[1].split(' ').map(Number);

const getDigit = (num, place) => Math.floor(Math.abs(num) / Math.pow(10, place)) % 10;

const digitCount = (num) => {
    if (num === 0) return 1;
    return Math.floor(Math.log10(Math.abs(num))) + 1;
}

const mostDigits = (nums) => {
    let max = 0;
    for (let num of nums) {
        max = Math.max(max, digitCount(num));
    }
    return max;
}

const radixSort = (arr) => {
    const maxDigits = mostDigits(arr);
    for (let k = 0; k < maxDigits; k++) {
        let digitBuckets = Array.from({length: 10}, () => []);
        for (let i = 0; i < arr.length; i++) {
            let digit = getDigit(arr[i], k);
            digitBuckets[digit].push(arr[i]);
        }
        arr = [].concat(...digitBuckets);
    }
    return arr;
}

console.log(radixSort(arr).join(' '));