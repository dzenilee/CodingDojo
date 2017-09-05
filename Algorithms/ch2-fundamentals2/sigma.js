//Implement function sigma(num) that given a number, returns the sum of all positive integers up to number (inclusive).
function sigma(num){
  sum = 0;
  for (var i = 1; i <= num; i++){
    sum += i
  }
  console.log(sum);
}

sigma(20);
