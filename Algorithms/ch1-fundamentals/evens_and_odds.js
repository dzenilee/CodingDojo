//Create a function that accepts an array. Every time that array has three odd values in a row, print "That’s odd!" Every time the array has three evens in a row, print "Even more so!"

function evens_and_odds(arr){
  for (i = 0; i < arr.length - 3; i++){
    if (arr[i] % 2 == 1 && arr[i+1] % 2 == 1 && arr[i+2] % 2 == 1){
      return "That's odd!"
    } else if (arr[i] % 2 == 0 && arr[i+1] % 2 == 0 && arr[i+2] % 2 == 0){
      return "Even more so!"
    }
  }
}

console.log(evens_and_odds([4, 3, 5, 2, 2, -6, 3, 4, 1, 10])); //Even more so!
