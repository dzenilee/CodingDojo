//Given an array and a value Y, count and print the number of array values greater than Y.
function greater_than(arr, Y){
  var count = 0;
  for (var i = 0; i < arr.length; i++){
    if (arr[i] > Y){
      count++;
    }
  } console.log(count);
}

greater_than([4, 5, 0, 23, 22, 1, 2], 3);
