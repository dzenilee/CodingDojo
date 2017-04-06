// Create a function that, given a string, returns the string's acronym (first letters only, capitalized).
// Given "Live from New York, it's Saturday Night!" returns "LFNYISN".

function acronyms(str){
  var into_arr = str.split(" "); //returns list of words in string: //[ 'Live', 'from', 'New', 'York,', 'it\'s', 'Saturday', 'Night!'
  var arr = [];
  for (var i = 0; i < into_arr.length; i++){
    var first_letter = into_arr[i].toUpperCase()[0];
    arr.push(first_letter);
  }
  return arr.join("") //LFNYISN
}


str = "Live from New York, it's Saturday Night!"
console.log(acronyms(str));
