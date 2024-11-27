const fs = require('fs')
const n = fs.readFileSync(0).toString().trim()

const MAX_NUMBER = 45;
const memo = new Array(MAX_NUMBER).fill(-1);

function fibbo(n) {
  if (memo[n] !== -1) {
    return memo[n];
  }
  if (n <= 2) {
    return 1;
  } else {
    return fibbo(n - 1) + fibbo(n - 2);
  }
}


console.log(fibbo(Number(n)))