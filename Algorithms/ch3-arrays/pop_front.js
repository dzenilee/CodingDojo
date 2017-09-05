//Given an array, remove and return the value at the beginning of the array. Do this without using any built-in array methods except pop().

var arr1 = ['gaming_fun', 'algos', 25, '...!']

function popFront(arr, val){
  arr[0] = val;
  return arr;
}

console.log(popFront(arr1, 'NEW_VAL'));
