// Accept a string and return the number of non-space characters found in the string.

function countNonSpaces(str){
  var count = 0;
  for (var char = 0; char < str.length; char++){
    if (str[char] != " "){
      count++;
    }
  }
  return count;
}

var str = "Honey pie, you are driving me crazy"
// console.log(str.length); //35
console.log(countNonSpaces(str)); //should return 29 (not 35) check:) 
