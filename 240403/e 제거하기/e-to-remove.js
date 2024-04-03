const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

let i = 0
while (true) {
    if (input[i] == 'e') {
        console.log(input.slice(0,i) + input.slice(i+1))
        break;
    }
    else {
        i += 1
    }
}