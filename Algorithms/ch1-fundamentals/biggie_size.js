// Given an array, write a function that changes all positive numbers in the array to “big”.
//
// Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1,"big","big",-5].

function biggie(array){
  var new_array = [];
  for (i = 0; i < array.length; i++){
    if (array[i] > 0){
      new_array[i] = "big";
    } else {
      new_array[i] = array[i];
    }
  }
  console.log(new_array);
}

biggie([3, 3, 4, -1]);
biggie([-1, 3, 5, -5]);
