const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const n = Number(input[0])

let people = []

class Person {
    constructor(name, height, weight) {
        this.name = name;
        this.height = height;
        this.weight = weight;
    }
}

for (let i = 1; i < n+1; i++) {
    const [name, height, weight] = input[i].split(' ')
    people.push(new Person(name, Number(height), Number(weight)))
}

people.sort((cur, prev) => cur.height - prev.height)

for (let j = 0; j < n; j++) {
    console.log(people[j].name + ' ' + people[j].height + ' ' + people[j].weight)
}