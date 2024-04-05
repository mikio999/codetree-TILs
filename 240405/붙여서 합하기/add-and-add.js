const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(' ')

const AB = input[0] + input[1]
const BA = input[1] + input[0]

console.log(Number(AB) + Number(BA))