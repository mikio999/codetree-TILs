class Product {
    constructor(name, code) {
        this.name = name;
        this.code = code;
    }
}

const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split(' ')

const product1 = new Product("codetree", "50")
const product2 = new Product(input[0], input[1])

console.log(`product ${product1.code} is ${product1.name}`)
console.log(`product ${product2.code} is ${product2.name}`)