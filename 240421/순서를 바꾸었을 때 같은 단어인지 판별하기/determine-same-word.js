const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

console.log(input[0].split('').sort().join('') == input[1].split('').sort().join('') ? 'Yes' : 'No')