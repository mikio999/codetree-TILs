const n = 5
let grid = Array(n).fill(0).map(() => Array(n).fill(0))

for (let i = 0; i < 5; i ++) {
    for (let j = 0; j < 5; j ++) {
        if ((i == 0) || (j == 0)) {
            grid[i][j] = 1
        }
        else {
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
        }
    }
}

for (let k =0; k < n; k++) {
    let str = ''
    for (let g = 0; g < n; g++) {
        str += grid[k][g] + ' '
    }
    console.log(str)
}