const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)

const n = Number(input[0])

let students = []

class Student {
    constructor(name, subject1, subject2, subject3) {
        this.name = name;
        this.subject1 = subject1;
        this.subject2 = subject2;
        this.subject3 = subject3;
    }
}

for (let i = 1; i < n+1; i++) {
    const [name, subject1, subject2, subject3] = input[i].split(' ')
    students.push(new Student(name, Number(subject1), Number(subject2), Number(subject3)))
}

function cmp(a, b) {
    return (a.subject1 + a.subject2 + a.subject3) - (b.subject1 + b.subject2 + b.subject3)
}

students.sort(cmp)

for (let j=0; j<n; j++) {
    console.log(`${students[j].name} ${students[j].subject1} ${students[j].subject2} ${students[j].subject3}`)
}