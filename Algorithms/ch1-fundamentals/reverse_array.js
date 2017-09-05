// Given array, write a function that reverses values, in-place.
//
// Example: reverse([3,1,6,4,2]) returns same array, containing [2,4,6,1,3].

function reverse(arr){
  var new_arr = [];
  for (var i = arr.length-1; i >= 0; i--){
    new_arr.push(arr[i]);
  }
  console.log(new_arr); //[2,4,6,1,3]
}

reverse([3,1,6,4,2]);
