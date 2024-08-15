const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const n = Number(input[0])

let commands = []
for (let i = 1; i < n+1; i++) {
    let command = input[i].split(' ')
    commands.push(command)
}

const m = new Map();

for (let j=0; j<n; j++) {
    if (commands[j][0] === 'add') {
        m.set(Number(commands[j][1]), Number(commands[j][2]))
    }
    else if (commands[j][0] === 'find') {
        if (m.has(Number(commands[j][1]))) {
            console.log(m.get(Number(commands[j][1])))
        }
        else if(!m.has(Number(commands[j][1]))) {
            console.log('None')
        }

    }
    else if (commands[j][0] === 'remove') {
        if (m.has(Number(commands[j][1]))) {
            m.delete(Number(commands[j][1]))
        }
    }
}