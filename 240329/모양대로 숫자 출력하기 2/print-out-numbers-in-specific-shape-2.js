const fs = require('fs')
const n = Number(fs.readFileSync(0).toString().trim())

let number = 2

for (let i=0; i < n; i ++) {
    let row = ''
    for (let j=0; j<n; j++) {
        row += number + ' '
        number += 2
        if (number > 8) {
            number = 2
        }
    }
    console.log(row)
}