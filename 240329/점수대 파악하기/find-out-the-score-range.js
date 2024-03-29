const fs =require('fs')
const input = fs.readFileSync(0).toString().split(' ').map(Number)

let cnt = [0,0,0,0,0,0,0,0,0,0,0]

for (let i = 0; i < 100; i++) {
    if (input[i] === 0) break;
    if (input[i] < 10) continue;
    cnt[parseInt(input[i] /10)]++;
}

for (let i = 10; i >= 1; i--) {
    console.log(i + "0 - " + cnt[i])
}