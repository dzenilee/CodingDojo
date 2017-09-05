//Given an array arr and a number num, multiply all values in arr by num, and return the changed array arr.

function scale_array(arr, num){
  var new_arr = [];
  for (var i = 0; i < arr.length; i++){
    new_arr.push(arr[i] * num);
  }
  console.log(new_arr);
}

scale_array([3, 2, -4], 3); 
