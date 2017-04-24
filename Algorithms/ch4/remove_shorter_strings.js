//Given a string array and value (length), remove any strings shorter than length from the array.

function remove(arr, val){
  var newArray = [];
  for (var i = 0; i < arr.length; i++){
    if (arr[i].length >= val){ //if length of element in array is >= val
      newArray.push(arr[i]); ///then include it in newArray
    }
  }
  return newArray;
}

var array = ['nonononono', 'yes', 'really?', 'meh', 'love!']
console.log(remove(array, 6))
