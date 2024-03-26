const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split('\n')

const n = Number(input[0])
const numbers = input[1].split(' ')

let num_list = []
for (i=0; i<n; i++) {
    num_list.push(Number(numbers[i]))
}

let answer = []
while (num_list.length >= 1) {
    let maxNum = Math.max(...num_list)
    let index = num_list.indexOf(maxNum)
    answer.push(index+1)
    num_list = num_list.slice(0,index)

}

console.log(answer.join(' '))