//Given an array and an additional value, insert this value at the beginning of the array. Do this without using any built-in array methods.

var arr1 = ['gaming_fun', 'algos', 25, '...!']

function pushFront(arr, val){
  for (var i = 0; i < arr.length; i++){
    i += 1;
  }
  arr[0] = val;
  return arr; 
}

console.log(pushFront(arr1, 'NEW_VAL'));
