const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const n = Number(input[0])

let commands = []

for (let i=1; i <= n; i++) {
    commands.push(input[i].split(' '))
}

let x = 0, y =0;

for (let i=0; i < n; i++) {
    if (commands[i][0] === 'N') {
        y += parseInt(commands[i][1])
    }
    else if (commands[i][0] === 'E') {
        x += parseInt(commands[i][1])
    }
    else if (commands[i][0] === 'S') {
        y -= parseInt(commands[i][1])
    }
    else if (commands[i][0] === 'W') {
        x -= parseInt(commands[i][1])
    }
}

console.log(x, y)