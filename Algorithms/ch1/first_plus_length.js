//Given an array, return the sum of the first value in the array, plus the array’s length. What happens if the array’s first value is not a number, but a string (like "what?") or a boolean (like false).

function first_plus_length(array){
  return array[0] + array.length;
}

console.log(first_plus_length([32, 34, 11, 2]))
