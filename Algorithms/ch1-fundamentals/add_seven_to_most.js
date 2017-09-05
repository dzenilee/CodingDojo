//Build function that accepts array. Return a new array with all values except first, adding 7 to each. Do not alter the original array.

function add_seven_to_most(arr){
  var new_arr = [];
  for (var i = 0; i < arr.length; i++){
    if (i != 0){
      new_arr.push(arr[i] + 7);
    }
  }
  return new_arr;
}

add_seven_to_most([3, 4, 2, -2, 3]);
