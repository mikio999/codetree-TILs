class Bomb {
    constructor(code, color, sec) {
        this.code = code;
        this.color = color;
        this.sec = sec;
    }
}

const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(' ')
const bomb1 = new Bomb(input[0], input[1], input[2])

console.log(`code : ${bomb1.code} \ncolor : ${bomb1.color} \nsecond : ${bomb1.sec}`)