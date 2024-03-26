const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
let n = Number(input);

console.log((n%2===1 && n%3===0) || (n%2===0 && n%5===0))