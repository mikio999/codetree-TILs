const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const n = Number(input[0])

class Weather {
    constructor(date, day, condition){
    this.date = date;
    this.day = day;
    this.condition = condition;
    }
}

let answer = new Weather('9999-99-99', '', '')

for (let i = 1; i < n+1; i++) {
    const [date, day, condition] = input[i].split(' ')
    const forecast = new Weather(date, day, condition);
    if (condition === 'Rain') {
        if (answer.date >= forecast.date) {
            answer = forecast
        }
    }
}

console.log(answer.date, answer.day, answer.condition)