//Create a function that, given an input string str, returns a boolean whether parentheses in str are valid. Valid sets of parentheses always open before they close, for example. For "Y(3(p)p(3)r)s", return true. Given "N(0(p)3", return false: not every parenthesis is closed." Given "N(0)t )_0(k", return false, because the underlined ")" is premature: there is nothing open for it to close.

var txt = "Y(3(p)p(3)r)s" //true
var txt2 = "N(0)t)0(k" //false
var txt3 = "N(0(p)3" //false

function parensValid(str){
  var parensOnly = ''
  for (var i = 0; i < txt.length; i++){
    if (str[i] == '(' | str[i] == ')'){
      parensOnly += str[i];
    }
  }
  console.log('all parens: ', parensOnly);
  if (parensOnly.length % 2 != 0){
    return false;
  } else {
    firstHalf = parensOnly.slice(0, parensOnly.length/2);
    secondHalf = parensOnly.slice(parensOnly.length/2, parensOnly.length);
    console.log('first half:  ', firstHalf);
    console.log('second half: ', secondHalf);
    for (var f = 0; f < firstHalf.length; i++){
      for (var s = secondHalf.length-1; secondHalf.length >= 0; i--){
        if (firstHalf[f] != secondHalf[s]){
          return true;
        }
        else {
          return false;
        }
      }
    }
  }
}

console.log(parensValid(txt));
console.log(parensValid(txt2));
console.log(parensValid(txt3));
