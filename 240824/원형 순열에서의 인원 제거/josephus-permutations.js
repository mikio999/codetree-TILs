const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(' ')
let N = Number(input[0])
let K = Number(input[1])

let people = []
let answer = []
for (let i=1 ; i<=N ; i++) {
    people.push(i)
}

let index = 0;

while (people.length > 0) {
   index = (index + K - 1) % people.length;
   answer.push(people.splice(index, 1)[0])
}

console.log(answer.join(' '))