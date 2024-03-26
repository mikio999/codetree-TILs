const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()
let n = Number(input)

let cnt = 0

while (true) {

    if (n%2==0){
        n = n/2
        cnt += 1
    }
    else if (n===1) {
        break
    }
    else {
        n = 3*n + 1
        cnt += 1
    }
}

console.log(cnt)