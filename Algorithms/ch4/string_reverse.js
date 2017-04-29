// Implement reverseString(str) that, given string, returns that string with characters reversed. Given "creature", return "erutaerc". Tempting as it seems, do not use the built-in reverse()!

function reverseString(str){
  var newString = ""
  for (var i = str.length-1; i >= 0; i--){
    newString += str[i];
  }
  console.log(newString);
}

reverseString("string with characters reversed")
reverseString("creature")
