//Stan learned something today: that reducing an array’s .length immediately shortens it by that amount. Given array arr and number X, remove all except the last X elements, and return arr (changed and shorter). Given ([2,4,6,8,10],3), change the given array to [6,8,10] and return it.

function last_few(arr, num){
  for (i = 0; i < num-1; i++){
    arr.splice(arr[arr.length], 1); //array.splice(start, deleteCount)

  }
  console.log(arr);
}

last_few([2,4,6,8,10],3);
