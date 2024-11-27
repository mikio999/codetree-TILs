const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', function(line) {
  const n = parseInt(line.trim());
  const MAX_NUMBER = 45;
  const memo = new Array(MAX_NUMBER + 1).fill(0);

  memo[1] = 1;
  memo[2] = 1;

  for (let i = 3; i <= n; i++) {
    memo[i] = memo[i - 1] + memo[i - 2];
  }

  console.log(memo[n]);
  rl.close();
}).on('close', function() {
  process.exit();
});
