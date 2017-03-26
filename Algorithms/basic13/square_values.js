//Square each value in a given array, returning that same array with changed values.
function square(arr){
  var new_arr = [];
  for (var i = 0; i < arr.length; i++){
    new_arr.push(arr[i]*arr[i]);
  }
  console.log(new_arr);
}

square([3, 4, 22, 2.1]);
