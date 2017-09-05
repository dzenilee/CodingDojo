// Create a function that takes array of numbers. The function should print the lowest value in the array, and return the highest value in the array.

function low_high(array){
  var min = array[0]; //set min to the first item in array to start out
  var max = array[0];
  for (i = 1; i < array.length; i++){
    if (array[i] < min){
      min = array[i];
    }
    if (array[i] > max){
      max = array[i];
    }
  }
  console.log(min);
  return max; 
}

low_high([-15, 29, 30, -2]);
low_high([0, -4, 2, -6]);
low_high([35, -200, -200, -420, -420, 2, 1, 9]);
