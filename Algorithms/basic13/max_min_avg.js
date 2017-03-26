//Given an array, print the max, min and average values for that array.
function max_min_avg(arr){
  var max = arr[0];
  var min = arr[0];
  var sum = 0;
  for (var i = 1; i < arr.length; i++){
    sum += arr[i]
    if (arr[i] > max){
      max = arr[i];
    } else {
      min = arr[i];
    }
  } console.log(max, min, (sum+arr[0])/arr.length);
}

max_min_avg([3, 0, 10, -2]);
