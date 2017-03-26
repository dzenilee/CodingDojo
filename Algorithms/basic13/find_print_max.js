//Given an array, find and print its largest element.
function find_max(arr){
  var max = arr[0];
  for (var i = 1; i < arr.length; i++){
    if (arr[i] > max){
      max = arr[i];
    }
  } console.log(max);
}

find_max([11, 22, 5, 1]);
