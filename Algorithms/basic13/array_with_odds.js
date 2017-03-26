//Create an array with all the odd integers between 1 and 255 (inclusive).
function odds_array(){
  var new_arr = [];
  for (var int = 1; int <= 255; int++){
    if (int % 2 != 0){
      new_arr.push(int);
    }
  }
  console.log(new_arr);
}

odds_array();
