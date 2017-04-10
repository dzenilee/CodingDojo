// Create a function that returns a boolean whether the string is a strict palindrome. For "a x a" or "racecar", return true.


//Do not ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return false.
function isPalindromeStrict(str){
  var reversedStr = ""
  for (var i = str.length-1; i >= 0; i--){
    reversedStr += str[i];
  }
  console.log(reversedStr);
  if (reversedStr == str){
    return true;
  }
  return false;
}

// console.log(isPalindromeStrict("racecar")); //true
// console.log(isPalindromeStrict("oho!")); //false

//DO ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return true.
//still working
function isPalindrome(str){
  var reversedStr = "";
  // var ignore = ["!", ",", ".", "!", " "];
  str.toLowerCase();
  for (var i = str.length-1; i >= 0; i--){
      reversedStr += str[i];
  }
  for (var j = 0; j < str.reversedStr; j++){
    if (reversedStr[j] != ','){
      return reversedStr;
    }
  }
}

console.log(isPalindrome("race,car"));
