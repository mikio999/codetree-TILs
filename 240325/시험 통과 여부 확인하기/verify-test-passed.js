const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

n = Number(input)

if (n >= 80) {
    console.log('pass')
}
else {
    console.log(`${80-n} more score`)
}