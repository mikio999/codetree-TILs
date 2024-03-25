const fs = require('fs')
const n = Number(fs.readFileSync(0).toString().trim())

if (n < 0) {
    console.log('ice')
}
else if (n < 100) {
    console.log('water')
}
else {
    console.log('vapor')
}