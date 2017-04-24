// Kaitlin sees beauty in numbers, but also believes that less is more. Implement sumToOne(num) that sums a given integer's digits repeatedly until the sum is only one digit. Return that one-digit result.

// Example: sumToOne(928) returns 1, because 9+2+8 = 19, then 1+9 = 10, then 1+0 = 1.

//still working 
function sumToOne(num){
  var string_num = num.toString();
  var sum = 0;
  for (var i = 0; i < string_num.length; i++){
    sum += parseInt(string_num[i]); //9
    console.log(sum); //19
  }
  sumToOne(sum);
}

sumToOne(928);

// var num = 928
// console.log(num.toString()); //928
// console.log(typeof(num.toString())); //string
// console.log(num.toString().length); //3 (length of string)
