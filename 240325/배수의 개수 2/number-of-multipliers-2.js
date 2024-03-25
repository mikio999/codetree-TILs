const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

cnt = 0

for (i = 0; i < 10; i++) {
    if (Number(input[i])%2 == 1) {
        cnt += 1
    }
}

console.log(cnt)