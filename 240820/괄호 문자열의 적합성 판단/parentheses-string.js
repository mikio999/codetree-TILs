const fs = require('fs')
const commands = fs.readFileSync(0).toString().trim().split('')

let stack = []

commands.forEach((item) => {
    if (item === '(') {
        stack.push('(')
    }
    else {
        if (stack[stack.length-1] === '(') {
            stack.pop()
        }
    }
})

if (stack.length === 0) {
    console.log('Yes')
}
else {
    console.log('No')
}