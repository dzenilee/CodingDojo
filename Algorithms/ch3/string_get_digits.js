// Create a JavaScript function that given a string, returns the integer made from the string's digits.
function getDigits(str){
  var newInt = "";
  var num = "0123456789";
  for (var i = 0; i < str.length; i++){
    for (var num = 0; num < 10; num++){
      if (str[i] == num){
        newInt += str[i];
      }
    }
  }
  return parseInt(newInt);
}

str = "hdj2ellosdk399fjsdlfj42skdjfei341"
console.log(getDigits(str)); //239942341

str2 = "hdj2ellosdk39 9fjsdlfj42skdjfei341" //<-- there's a space
console.log(getDigits(str2)); //239 <-- why?
