const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()
n = Number(input)
cnt = 0
for (i = 0; i <= n; i++) {
    if (i%2 == 0){
        continue
    }
    else if (i%3 == 0) {
        continue
    }
    else if (i%5 == 0) {
        continue
    }
    else {
        cnt += 1
    }
}

console.log(cnt)