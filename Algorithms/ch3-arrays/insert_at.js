//Given an array, index, and additional value, insert the value into the array at given index. Do this without using built-in array methods. You can think of PushFront(arr,val) as equivalent to InsertAt(arr,0,val).

var arr1 = ['gaming_fun', 'algos', 25, '...!']

function insertAt(arr, index, val){
  arr[index] = val;
  return arr;
}

console.log(insertAt(arr1, 2, 'NEW_VAL')); //[ 'gaming_fun', 'algos', 'NEW_VAL', '...!' ]
console.log(insertAt(arr1, 7, 'NEW_VAL')); //[ 'gaming_fun', 'algos', 'NEW_VAL', '...!', , , , 'NEW_VAL' ]
