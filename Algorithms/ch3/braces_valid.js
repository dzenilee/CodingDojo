//Given a sequence of parentheses, braces, and brackets, determine whether it is valid. Example:

var txt1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!" // true.
var txt2 = "D(i{a}l[ t]o)n{e" // false.
var txt3 = "A(1)s[O(n]0{t) 0}k"  // false

// function bracesValid(str){
//   var left_paren = '('
//   var right_paren = ')'
//   var left_brace = '{'
//   var right_brace = '}'
//   var left_bracket = '['
//   var right_bracket = ']'
//
//   var parens = [ left_paren, right_paren ];
//   var braces = [ left_brace, right_brace ];
//   var brackets = [ left_bracket, right_bracket ];
//
//   for (var i = 0; i < str.length; i++){
//     for (var j = 0; j < str.length; j++){
//       if (str[i] == parens[j]){
//         console.log(str[i]);
//       }
//     }
//   }
// }

// bracesValid(txt1)

function bracesValid(str){
  var bracketCounter, braceCounter, parenCounter == 0;
  for (var i = 0; i < str.length; i++){
    if (str[i] == "("){
      parenCounter++;
    } else if (str[i] == "["){
      bracketCounter++;
    } else if (str[i] == "{"){
      braceCounter++;
    } 
  }
}
