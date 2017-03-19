//Given array, create a function to return a new array where each value in the original has been doubled. Calling double([1,2,3]) should return [2,4,6] without changing original.

function double(arr){
  var doubled_arr = [];
  for (i = 0; i < arr.length; i++){
    doubled_arr.push(arr[i]*2);
  }
  console.log(doubled_arr);
}

double([3, 2, 12, 4]);
