//Print integers from 0 to 255, and with each integer print the sum so far.
var sum = 0;
for (var int = 0; int < 255; int++){
  sum += int;
  console.log(int, sum);
}
