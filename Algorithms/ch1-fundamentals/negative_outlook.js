//Given an array, create and return a new one containing all the values of the provided array, made negative (not simply multiplied by -1). Given [1,-3,5], return [-1,-3,-5].

function negative(arr){
  var new_arr = [];
  for (var i = 0; i < arr.length; i++){
    if (arr[i] > 0){ //if the value is positive,
      new_arr.push(arr[i] * -1); //multiply the value by -1
    } else {
      new_arr.push(arr[i]);
    }
  }
  console.log(new_arr);
}

negative([1, 23, -3, 41, -5]);
