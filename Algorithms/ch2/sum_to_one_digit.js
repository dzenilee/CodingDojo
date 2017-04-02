// Kaitlin sees beauty in numbers, but also believes that less is more. Implement sumToOne(num) that sums a given integer's digits repeatedly until the sum is only one digit. Return that one-digit result.

// Example: sumToOne(928) returns 1, because 9+2+8 = 19, then 1+9 = 10, then 1+0 = 1.
function sumToOne(num){
  var string_num = num.toString();
  var sum = 0;
    for (var i = 0; i < string_num.length; i++){
      sum += parseInt(string_num[i]);
    }
    console.log(sum); //19
    console.log(typeof(sum)); //number

}

sumToOne(928); //19 --> 10 --> 1
