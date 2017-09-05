//Swap positions of successive pairs of values of given array. If the length is odd, do not change the final element. For [1,2,3,4], return [2,1,4,3]. For example, change input ["Brendan",true,42] to [true,"Brendan",42]. As with all array challenges, do this without using any built-in array methods.

var arr1 = ['gaming_fun', 'algos', 25, '...!', 3333]

function helper(arr){
  var i = 0;
  var temp1 = arr[i];
  var temp2 = arr[i+1];
  arr[i] = temp2;
  arr[i+1] = temp1;
}

function swapPairs(arr){
  //if even number of elements in arr:
  if (arr.length % 2 == 0){
    for (var i = 0; i < arr.length; i+=2){
      helper(arr);
    }
  //else if odd number of elements in arr:
  } else if (arr.length % 2 != 0){
    for (var i = 0; i < arr.length-1; i+=2){
      helper(arr);
    }
  }
  return arr;
}

console.log(swapPairs(arr1));
