//Return the given array, after setting any negative values to zero.
function zero_out(arr){
  for (var i = 0; i < arr.length; i++){
    if (arr[i] < 0){
      arr[i] = 0;
    }
  } console.log(arr);
}

zero_out([4, 2, 4, 10, -2, 3, -7]); 
