const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const n = Number(input[0])

class Student {
    constructor(name, kor, eng, math) {
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
    }
}

let students = []

for (let i = 1; i < n+1; i++) {
    const [name, kor, eng, math] = input[i].split(' ')
    students.push(new Student(name, Number(kor), Number(eng), Number(math)))
}

function cmp(a,b) {
    if (a.kor !== b.kor) {
        return b.kor - a.kor
    }
    if (a.eng !== b.eng) {
        return b.eng - a.eng
    }
    return b.math - a.math
}

students.sort(cmp)

for (let j=0; j < n; j++) {
    console.log(`${students[j].name} ${students[j].kor} ${students[j].eng} ${students[j].math}`)
}