//You are passed an array containing strings. Working within that same array, replace each string with a number – the length of the string at previous array index – and return the array.

function prev_lengths(arr){
  var count = 0;
  var new_arr = [];
  for (var i = 0; i < arr.length; i++){
    if (i==0){
      new_arr.push(undefined);
    } else{
      new_arr.push(arr[i-1].length);
    }
  }
  return new_arr; 
}

prev_lengths(["whee", "wonderful", "coding", "is", "fun"]);
