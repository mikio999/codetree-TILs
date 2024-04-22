const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(' ')

class Mission {
    constructor(code,place,time) {
        this.code = code;
        this.place = place;
        this.time = time;
    }
}

const mission1 = new Mission(input[0], input[1], Number(input[2]))

console.log(`secret code : ${mission1.code}`)
console.log(`meeting point : ${mission1.place}`)
console.log(`time : ${mission1.time}`)