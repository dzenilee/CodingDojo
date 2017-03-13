// Create a function that accepts a number as an input. Return a new array that counts down by one, from the number (as array’s ‘zero’th element) down to 0 (as the last element). How long is this array?
function countdown(num) {
  for (var array = []; num >= 0; num--){
    array.push(num);
  }
  console.log(array);
}

countdown(15);
