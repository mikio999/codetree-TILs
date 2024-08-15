const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const n = Number(input[0])
const m = new Map();

for (let i = 1; i < n+1; i++) {
    const [command, k, v] = input[i].split(' ')

    if (command === 'add') {
        m.set(k,v);
    }
    else if (command === 'remove') {
        m.delete(k);
    }
    else if (command === 'find') {
        if (!m.has(k)) {
            console.log('None')
        }
        else {
            console.log(m.get(k))
        }
    }
}