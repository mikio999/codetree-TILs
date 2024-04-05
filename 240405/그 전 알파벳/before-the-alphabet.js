const fs = require('fs')
const input = fs.readFileSync(0).toString().trim()

const target = input.charCodeAt() - 1
const answer = (target !== 96 ? String.fromCharCode(target) : 'z')

console.log(answer)