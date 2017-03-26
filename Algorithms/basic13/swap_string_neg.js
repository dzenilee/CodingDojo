//Given an array of numbers, replace any negative values with the string 'Dojo'.
function swap_neg(arr){
  for (var i = 0; i < arr.length; i++){
    if (arr[i] < 0){
      arr[i] = 'Dojo'
    }
  } console.log(arr);
}

swap_neg([3, 4, -2, 1, -8]);
