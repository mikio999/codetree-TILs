const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(`\n`)
const target = input[0].split(' ')
let s = target[0]
const q = Number(target[1])

let ans = s.split('')
for (let i = 1; i < q+1; i++ ) {
    let question = input[i].split(' ')
    if (question[0] === '1' ) {
        const a = Number(question[1]) - 1
        const b = Number(question[2]) - 1
        ans[a] = s[b]
        ans[b] = s[a]
        console.log(ans.join(''))
    }
    else if (question[0] === '2') {
        const a = question[1]
        const b = question[2]
        ans = ans.join('').replaceAll(a,b)
        console.log(ans)
    }
}