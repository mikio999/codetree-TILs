const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const N = input[0]

class Stack {
    constructor() {
        this.items = [];
    }
    push(item) {
        this.items.push(item);
    }
    pop() {
        return this.items.pop();
    }
    empty() {
        return this.items.length === 0 ? 1 : 0;
    }
    size() {
        return this.items.length;
    }
    top() {
        return this.items[this.items.length - 1]
    }
}

let stack = new Stack()
const executeCommands = (command,x=0) => {
    switch(command) {
        case 'push' :
        stack.push(x)
        break;
        case 'pop' :
        console.log(stack.pop());
        break;
        case 'size' :
        console.log(stack.size());
        break;
        case 'empty' :
        console.log(stack.empty());
        break;
        case 'top' :
        console.log(stack.top());
        break;
        default :
        break;
    }
}


for (let i = 1; i <= N; i++) {
    const command = input[i]
    if (command.slice(0,4) === 'push') {
        executeCommands('push', Number(command.slice(5,)))
    }
    else {
        executeCommands(command)
    }
}