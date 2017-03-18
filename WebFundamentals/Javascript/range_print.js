// Create a function that can take a start point, end point, and skip amount, to print all numbers in the range.
//
// (Should go UP TO, but NOT INCLUDING the end point)


function printRange(start, end, skip_amount){
  for (var i = start; i < end; i += skip_amount){
    console.log(i);
  }
}

printRange(-6, 12, 4); //-6, -2, 2, 6, 10
