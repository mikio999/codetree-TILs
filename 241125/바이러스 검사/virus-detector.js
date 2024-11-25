const fs = require('fs')
const input = fs.readFileSync(0).toString().split(`\n`)

const n = Number(input[0])
const peopleInStores = []
for (let i=0; i<n; i++) {
    peopleInStores.push(Number(input[1].split(' ')[i]))
}
const maxLeaderCapacity = Number(input[2].split(' ')[0])
const maxMemberCapacity = Number(input[2].split(' ')[1])

let totalCount = 0;

for (let i = 0; i < n; i++) {
  if (peopleInStores[i] <= maxLeaderCapacity) {
    totalCount += 1;
  } else {
    const peopleManagedByMembers = peopleInStores[i] - maxLeaderCapacity;
    const fullMemberGroups = Math.floor(
      peopleManagedByMembers / maxMemberCapacity
    );
    totalCount += 1 + fullMemberGroups;
    if (peopleManagedByMembers % maxMemberCapacity > 0) {
      totalCount += 1;
    }
  }
}

console.log(totalCount);
