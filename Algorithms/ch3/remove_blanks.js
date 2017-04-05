// Create a function that given a string, returns all of that string's contents, but without blanks.

function removeBlanks(str){
  var newString = ""
  for (var i = 0; i < str.length; i++){
    if (str[i] != " "){
      newString += str[i];
    }
  }
  return newString;
}

console.log(removeBlanks("I Love Coding!"));
