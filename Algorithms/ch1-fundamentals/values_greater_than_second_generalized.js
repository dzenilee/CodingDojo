//Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value. Print how many values this is. What will you do if the array is only one element long?
var new_array = [];
var count = 0;
function greater_second_generalized(array){
  for (var i = 0; i < array.length; i++){
    if (array[i] > array[1]){
      new_array.push(array[i]);
      count++;
    }
  }
  console.log(new_array);
  console.log('count: '+count);
}

greater_second_generalized([13, 4, 22, 10, 3]);
