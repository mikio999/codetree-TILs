const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(' ')

const first = input[0]
const second = input[1]

const firstCode = first.charCodeAt(0)
const secondCode = second.charCodeAt(0)

console.log(firstCode + secondCode, firstCode >= secondCode ? firstCode - secondCode : secondCode - firstCode)