#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found:', process.argv[2]);
} else {
  console.log('Arguments found:', process.argv.slice(2).join(', '));
}
