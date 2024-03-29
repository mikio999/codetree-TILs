const fs =require('fs')
const input = fs.readFileSync(0).toString().split(' ').map(Number)
let cnt = [0,0,0,0,0,0,0,0,0,0]

for (let i = 0; i < input.length; i++ ) {
    if (input[i] > 10) {
        if (input[i] === 100) {
            cnt[0] += 1
        }
        else if (input[i] >= 90) {
            cnt[1] += 1
        }
        else if (input[i] >= 80) {
            cnt[2] += 1
        }
        else if (input[i] >= 70) {
            cnt[3] += 1
        }
        else if (input[i] >= 60) {
            cnt[4] += 1
        }
        else if (input[i] >= 50) {
            cnt[5] += 1
        }
        else if (input[i] >= 40) {
            cnt[6] += 1
        }
        else if (input[i] >= 30) {
            cnt[7] += 1
        }
        else if (input[i] >= 20) {
            cnt[8] += 1
        }
        else if (input[i] >= 10) {
            cnt[9] += 1
        }
    }
}

for (let j=0; j<10; j++) {
    console.log(`${100-(j*10)} - ${cnt[j]}`)
}