const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()


console.log(input.slice(0,2) + input.slice(3,-2) + input.slice(-1))