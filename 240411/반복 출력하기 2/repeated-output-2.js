const fs = require('fs')
const N = Number(fs.readFileSync(0).toString().trim())
function printHello(n){
    if (n === 0) return;
    printHello(n-1);
    console.log('HelloWorld')
}

printHello(N);