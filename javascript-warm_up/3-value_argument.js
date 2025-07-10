#!/usr/bin/node
let index = 0;
process.argv.forEach((val, index1) => {if (index1 > 1) console.log(val); index++;});
if (index < 3)
    console.log('No argument');
