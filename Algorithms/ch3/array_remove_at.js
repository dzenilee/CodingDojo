//Given an array and an index into array, remove and return the array value at that index. Do this without using built-in array methods except for the pop(). Think of PopFront(arr) as equivalent to RemoveAt(arr,0).

var arr1 = ['gaming_fun', 'algos', 25, '...!', 1111]

function removeAt(arr, index){
  var reducedArr = [];
  for (var i = 0; i < arr.length; i++){
    if (i != index){
      reducedArr.push(arr[i]);
    }
  }
  return reducedArr;
}

console.log(removeAt(arr1, 3));
