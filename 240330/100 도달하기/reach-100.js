const fs = require('fs')
const n = Number(fs.readFileSync(0).toString().trim())

let numbers = [1,n]

let number = 0
let index = 2

while (true) {
    if (number < 100) {
        number = numbers[index-1] + numbers[index-2]
        numbers.push(number)
        index += 1
    }
    else {
        break
    }
}

str = ''
for (let i = 0; i < numbers.length; i++ ) {
    str += numbers[i] + ' '
}

console.log(str)