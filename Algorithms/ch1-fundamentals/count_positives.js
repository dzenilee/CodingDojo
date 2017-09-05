//Given array of numbers, create function to replace last value with number of positive values.

function positives(arr){
  var count = 0;
  for (i = 0; i < arr.length; i++){
    if (arr[i] > 0){
      count++;
    }
  }
  arr[arr.length-1] = count;
  console.log(arr);
}

positives([-3, 4, 5, -2, 3, 3, -10]);
