// Make a function that copies an array, ONLY accepting the items that are numbers.
//
// IT SHOULD RETURN A NEW ARRAY
// Use typeof to determine type (ex: typeof 24 === "number" would be true)

//var newArray = numbersOnly([1, "apple", -3, "orange", 0.5]);
// newArray is [1, -3, 0.5]

function num_only(arr){
  var new_arr = [];
  for (i = 0; i < arr.length; i++){
    if (typeof(arr[i]) === 'number'){
      new_arr.push(arr[i]);
    }
  }
  console.log(new_arr);
}

num_only([1, "apple", -3, "orange", 0.5]);
