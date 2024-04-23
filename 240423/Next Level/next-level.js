const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(' ')
const a = input[0]
const b = Number(input[1])

class Game {
    constructor(id = 'codetree', level = 10) {
        this.id = id;
        this.level =level;
    }
}

const account1 = new Game()
console.log(`user ${account1.id} lv ${account1.level}`)
const account2 = new Game(a, b)
console.log(`user ${account2.id} lv ${account2.level}`)