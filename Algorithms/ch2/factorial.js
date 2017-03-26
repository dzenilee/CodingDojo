//Just the Facts, ma'am. Factorials, that is. Write a function factorial(num) that, given a number, returns the product (multiplication) of all positive integers from 1 up to number (inclusive).
function factorial(num){
  var prod = 1;
  for (var i = 1; i <= num; i++){
    prod *= i;
  }
  console.log(prod);
}

factorial(6); 
