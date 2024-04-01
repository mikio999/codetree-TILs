const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

maxString = Math.max(input[0].length, input[1].length, input[2].length)
minString = Math.min(input[0].length, input[1].length, input[2].length)

console.log(maxString - minString)