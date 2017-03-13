//For [1,3,5,7,9,13], print values that are greater than its 2nd value. Return how many values this is.
var array = [1,3,5,7,9,13];
var count = 0;
for (var i = 0; i < array.length; i++){
  if (array[i] > array[1]) {
    console.log(array[i]);
    count++;
  }
  // don't put 'return' here. Because it ends the function.
}
return count; //this has to be outside the for loop because otherwise 'return' blocks all other printing.

//console.log(count);
