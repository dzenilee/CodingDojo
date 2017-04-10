// Create a function that returns a boolean whether the string is a strict palindrome. For "a x a" or "racecar", return true.

//Do not ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return false.
function isPalindromeStrict(str){
  var reversedStr = ""
  for (var i = str.length-1; i >= 0; i--){
    reversedStr += str[i];
  }
  if (reversedStr == str){
    return true;
  }
  return false;
}
console.log(isPalindromeStrict("racecar")); //true
console.log(isPalindromeStrict("oho!")); //false

//DO ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return true.
function isPalindrome(str){
  var newStr = "";
  var ignore = ["!", ",", ".", "!", " "];
  str = str.toLowerCase();
  for (var i = 0; i < str.length; i++){
    if (ignore.indexOf(str[i]) > -1){
      continue;
    } else {
      newStr += str[i];
    }
  }
  var reversedStr = "";
  for (var j = newStr.length-1; j >= 0; j--){
    reversedStr += newStr[j];
  }
  if (reversedStr == newStr){
    return true;
  }
  return false;
}

console.log(isPalindrome("Rac.ecar.")); //true
console.log(isPalindrome("oho!")); //true
