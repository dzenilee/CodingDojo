// Build a function that takes array of numbers. The function should print second-to-last value in the array, and return first odd value in the array.

function one_another(array){
  console.log(array[array.length-2]); //outside for loop.
  for (i = 0; i < array.length; i++){
    if (array[i] % 2 != 0){
      console.log(array[i]); //should return -3.
      break;
    }

  }
}

one_another([-4, -3, -3, 5, 2, 33, 20]);
one_another([100, -3, 502, 3042, 1]);
