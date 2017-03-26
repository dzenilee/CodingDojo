//Given an array, move all values forward by one index, dropping the first and leaving a '0' value at the end.
function shift(arr){
  new_arr = [];
  for (var i = 1; i < arr.length; i++){
    new_arr.push(arr[i]);
  }
  new_arr.push(0);
  console.log(new_arr);
}

shift([3, 4, 23, 1]);
