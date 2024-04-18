const fs = require('fs')
const target = fs.readFileSync(0).toString().trim().split('')

console.log(target.sort().join(''))