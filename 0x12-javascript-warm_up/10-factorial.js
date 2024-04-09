#!/usr/bin/node
function factorial (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
}

cosole.log(factorial(Number(process.argv[2])));
