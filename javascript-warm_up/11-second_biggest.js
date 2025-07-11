#!/usr/bin/node
let max1 = process.argv[2];
let max2 = process.argv[3];
if (process.argv[2] < process.argv[3]) {
  max1 = process.argv[3];
  max2 = process.argv[2];
}

for (let i = 4; i < process.argv.length; i++) {
  if (process.argv[i] < max1 && process.argv[i] > max2) {
    max2 = process.argv[i];
  } else if (process.argv[i] > max1) {
    max2 = max1;
    max1 = process.argv[i];
  }
}
if (process.argv.length > 3) { console.log(max2); } else { console.log('0'); }
