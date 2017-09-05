//Given array, swap first and last, third and third-tolast, etc. Input[true,42,"Ada",2,"pizza"] becomes ["pizza",42,"Ada",2,true]. Change [1,2,3,4,5,6] to [6,2,4,3,5,1].

function swap(arr){
  var temp = arr[i];
  var new_arr = [];
  for (var i = 0; i < arr.length; i+=2){
    arr[i] = arr[arr.length-i];
    new_arr.push(arr[i]);
    arr[arr.length-i] = temp;
    // new_arr.push(arr[arr.length-1]);
  }
  console.log(new_arr);
}

swap([1,2,3,4,5,6]);
