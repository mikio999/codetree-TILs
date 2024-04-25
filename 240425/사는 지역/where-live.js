const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const n = Number(input[0])

class Address {
    constructor(name, address, region) {
        this.name = name;
        this.address = address;
        this.region = region;
    }
}

let people = []

for (i=1; i<n+1; i++) {
     const [name, address, region] = input[i].split(' ');
    people.push(new Address(name, address, region));
}

let targetIdx = 0;
for (let i = 1; i < people.length; i++) {
    if (people[i].name > people[targetIdx].name) {
        targetIdx = i;
    }
}

// 결과 출력
console.log(`name ${people[targetIdx].name}`);
console.log(`addr ${people[targetIdx].address}`);
console.log(`city ${people[targetIdx].region}`);