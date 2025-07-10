#!/usr/bin/node
let trouve = 0;
let str= ''
process.argv.slice(2).forEach((val) => {str=str+' ' +val; trouve++;});
if (trouve === 0)
{
  console.log('No argument');
}
else
{
  console.log(str.slice(1));
}

