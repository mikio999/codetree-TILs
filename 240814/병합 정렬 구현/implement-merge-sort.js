const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(`\n`);

const n = Number(input[0]);
const arr = input[1].split(' ').map(Number);

function merge_sort(arr, low, high) {
    if (low < high) {
        let mid = Math.floor((low + high) / 2);
        merge_sort(arr, low, mid);
        merge_sort(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }
}

function merge(arr, low, mid, high) {
    let merged_arr = Array(high - low + 1);
    let i = low;
    let j = mid + 1;
    let k = 0;

    while (i <= mid && j <= high) {
        if (arr[i] <= arr[j]) {
            merged_arr[k++] = arr[i++];
        } else {
            merged_arr[k++] = arr[j++];
        }
    }

    while (i <= mid) {
        merged_arr[k++] = arr[i++];
    }
    while (j <= high) {
        merged_arr[k++] = arr[j++];
    }

    for (let s = 0; s < merged_arr.length; s++) {
        arr[low + s] = merged_arr[s];
    }
}

merge_sort(arr, 0, arr.length - 1);
console.log(arr.join(' '));