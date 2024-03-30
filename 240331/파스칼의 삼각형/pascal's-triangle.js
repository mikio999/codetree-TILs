const fs = require('fs')
const n = Number(fs.readFileSync(0).toString().trim())

const triangle = []

for (let i=1; i < n+1; i++ ) {
    triangle.push(Array(i).fill(1))
}

for (let i = 2; i < n; i ++ ){
    for (j = 1; j < i; j ++ ) {
        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    }
}

for (let i = 0; i < n; i ++ ) {
    let str = ''
    for (let j = 0; j < i+1; j ++ ) {
        str += triangle[i][j] + ' '
    }
    console.log(str)
}