//Given an array of numbers arr, add 1 to every second element, specifically those whose index is odd (arr[1], [3], [5], etc). Afterward, console.log each array value and return arr.

function increment(arr){
  for (var i = 0; i < arr.length; i++){
    if (i % 2 == 0){ //if index is odd
      console.log(arr[i]);
    } else {
      console.log(arr[i]+1);
    }
  }
  return arr;
}

increment([3, 4, 2, -2, 3]);
