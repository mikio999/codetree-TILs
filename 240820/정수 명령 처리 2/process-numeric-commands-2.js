class Queue {
    constructor(){
        this.q = [];
    }

    push(item) {
        this.q.push(item);
    }

    empty() {
        return this.q.length === 0;
    }

    size() {
        return this.q.length;
    }

    pop() {
        if(this.empty()) {
            return -1; 
        }

        return this.q.shift();
    }

    front() {
        if (this.empty()) {
            return -1; 
        }

        return this.q[0];
    }
}

const q = new Queue();
const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(`\n`);

const N = Number(input[0]);

for (let i = 1; i <= N; i++) {  
    let command = input[i].trim();

    if (command.startsWith('push')) {
        q.push(Number(command.split(' ')[1]));
    } 
    else if (command === 'front') {
        console.log(q.front());
    } 
    else if (command === 'size') {
        console.log(q.size());
    } 
    else if (command === 'empty') {
        console.log(q.empty() ? 1 : 0);  
    } 
    else if (command === 'pop') {
        console.log(q.pop());
    }
}