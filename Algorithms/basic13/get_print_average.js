//Analyze an array’s values and print the average.
function avg(arr){
  var sum = 0;
  for (var i = 0; i < arr.length; i++){
    sum += arr[i];
  }
  console.log(sum/arr.length);
}

avg([3, 4, 1, 50]);
