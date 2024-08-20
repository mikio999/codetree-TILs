const fs = require('fs')
const commands = fs.readFileSync(0).toString().trim().split('')

class Stack {
    constructor() {
        this.items = []
    }
    push(item) {
        this.items.push(item)
    }
    empty() {
        return this.items.length === 0;
    }
    size() {
        return this.items.length;
    }
    pop() {
        if (this.empty()) {
            throw new Error('Stack is empty')
        }
    }
    top() {
        if (this.empty()) {
            throw new Error ('Stack is empty')
        }

        return this.items[this.items.length - 1]
    }
}

const s = new Stack();

for (let char of commands) {
    if (char === '(') {
        s.push('(')
    } else {
        if (s.empty()) {
            console.log('No');
            process.exit(0)
        }

        s.pop()
    }
}

if (s.empty()) {
    console.log('Yes')
}
else {
    console.log('No')
}