//Given a sequence of parentheses, braces, and brackets, determine whether it is valid. Example:

var txt1 = "W(a{ts[}o(n{ c}o)m]e )h[e{r}e]!" // true (should this be false?) book typo?
var txt2 = "D(i{a}l[ t]o)n{e" // false.
var txt3 = "A(1)s[O(n]0{t) 0}k"  // false

function bracesValid(str){
  var check = [];
  for (var i = 0; i < str.length; i++){
    if (str[i] == "(" || str[i] == "[" || str[i] == "{"){
      check.push(str[i]);
    } else if (str[i] == ")" || str[i] == "]" || str[i] == "}"){
      if (str[i] == ")" && check[check.length-1] == "(" || str[i] == "}" && check[check.length-1] == "{" || str[i] == "]" && check[check.length-1]== "["){
        check.pop(); //if closed paren matches open paren, pop open paren
      } else {
        return false;
      }
    }
  }
  console.log(check);
  if (check.length){
    return false;
  }
  return true;
}

console.log(bracesValid("{([])}"));
// console.log(bracesValid(txt1));
// console.log(bracesValid(txt2));
// console.log(bracesValid(txt3));
