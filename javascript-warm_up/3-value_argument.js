#!/usr/bin/node
let trouve = 0;
process.argv.slice(2).forEach((val) => {console.log(val); trouve++;});
if (trouve === 0)
{
  console.log('No argument');
}

