//Create a function that accepts an array, and prints "yummy" each time one of the values is equal to "food". If no array elements are "food", then print "I'm hungry" once.

//Note: this is where you have to use counter. You want to do something ONCE after iterating.

function hungry(arr){
  var counter = 0;
  for (var i = 0; i < arr.length; i++){
    if (arr[i] == 'food'){
      counter++;
      console.log('yummy');
    }
  }
  if (counter == 0){
    console.log('I\'m hungry');
  }

}

hungry(['NOT_food', 'abc', 'x', 'coding']);
hungry(['food', 'NOT_food', 'food', 'x', 'coding', 'food']);
