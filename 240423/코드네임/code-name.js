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

agents.sort((a,b) => a-b)
console.log(agents[0].codeName, agents[0].score)