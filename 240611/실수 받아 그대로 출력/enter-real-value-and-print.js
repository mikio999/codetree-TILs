const fs = require('fs');
let a = fs.readFileSync(0).toString();
console.log((parseFloat(a)).toFixed(2));