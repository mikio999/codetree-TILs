const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const N = Number(input[0])

class Array {
    constructor() {
        this.items = []
    }
    push_back(A) {
        this.items.push(A)
    }
    pop_back() {
        this.items.pop()
    }
    size() {
        return this.items.length
    }
    get(k) {
        return this.items[k-1]
    }
}

let dynamicArray = new Array()

const executeCommands = (command, x=0) => {
    switch(command) {
        case 'push_back':
        dynamicArray.push_back(x)
        break;
        case 'pop_back':
        dynamicArray.pop_back()
        break;
        case 'size' :
        console.log(dynamicArray.size())
        break;
        case 'get' :
        console.log(dynamicArray.get(x))
        break;
        default :
        break;
    }
}

for (let i = 1; i <= N; i++) {
  const command = input[i];
  if (command.slice(0, 9) === "push_back") {
    executeCommands("push_back", Number(command.slice(10)));
  } else if (command.slice(0, 3) === "get") {
    executeCommands("get", Number(command.slice(4)));
  } else {
    executeCommands(command);
  }
}