const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(' ')

const a = input[0]
const b = Number(input[1])

console.log(a.charCodeAt(), String.fromCharCode(b))