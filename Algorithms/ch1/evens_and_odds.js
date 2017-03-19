//****NOT DONE. COME BACK TO THIS.*****

//Create a function that accepts an array. Every time that array has three odd values in a row, print "That’s odd!" Every time the array has three evens in a row, print "Even more so!"

function how_odd(arr){
  var odd_count = 0;
  var current = arr[0];
  for (i = 1; i < arr.length; i++){
    while (odd_count < 3) {
      if (arr[i] % 2 != 0 && current % 2 != 0){
        odd_count++;
      }
      break;
    }
  }
  if (odd_count == 3){
    console.log("That's odd!");
  }
}

how_odd([-2, 4, 3, 5, 3, 4, 1, 10]);
