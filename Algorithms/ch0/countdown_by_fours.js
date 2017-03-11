//Log positive numbers starting at 2016, counting down by fours (exclude 0), without a FOR loop.
function count_by_four(){
  var i = 2016;
  while (i > 0){
    console.log(i);
    i = i-4;
  }
}

count_by_four();
