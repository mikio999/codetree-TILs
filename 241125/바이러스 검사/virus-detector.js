const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const input = [];
rl.on('line', function(line) {
  input.push(line);
}).on('close', function() {
  const n = Number(input[0]);
  const peopleInStores = input[1].split(' ').map(Number);
  const capacities = input[2].split(' ');
  const maxLeaderCapacity = Number(capacities[0]);
  const maxMemberCapacity = Number(capacities[1]);

  let totalCount = 0;
  for (let i = 0; i < n; i++) {
    if (peopleInStores[i] <= maxLeaderCapacity) {
      totalCount += 1;
    } else {
      const peopleManagedByMembers = peopleInStores[i] - maxLeaderCapacity;
      const fullMemberGroups = Math.floor(peopleManagedByMembers / maxMemberCapacity);
      totalCount += 1 + fullMemberGroups;
      if (peopleManagedByMembers % maxMemberCapacity > 0) {
        totalCount += 1;
      }
    }
  }

  console.log(totalCount);
  process.exit();
});
