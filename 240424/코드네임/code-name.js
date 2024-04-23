class Agent {
    constructor (codeName, score) {
        this.codeName = codeName;
        this.score = score;
    }
}

const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)


let agents = [];

for (let i = 0; i < input.length; i ++) {
    let codeName = input[i].split(' ')[0]
    let score = Number(input[i].split(' ')[1])
    agents.push(new Agent(codeName, score))
}

let min_agent = 0

for (let j = 1; j< input.length; j++) {
    if (agents[min_agent].score > agents[j].score) {
        min_agent = j;
    }
}

console.log(agents[min_agent].codeName, agents[min_agent].score)