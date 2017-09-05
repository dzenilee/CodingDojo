/*
Return whether a given integer is prime. Prime numbers are only evenly divisible by themselves and 1. Many highly optimized solutions exist, however, for now, just create one that is easy to understand and debug.
*/

function isPrime(int){
  for (var i = 2; i < int; i++){
    if (int % i == 0){
      return false;
    } else {
      return true;
    }
  }
}

console.log(isPrime(23));
console.log(isPrime(13));
console.log(isPrime(17));
console.log(isPrime(12));
