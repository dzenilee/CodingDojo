//Add odd integers from -300,000 to 300,000, and console.log the final sum. Is there a shortcut?

var i = -300000;
var sum = 0;

while (i <= 300000){
  if (i % 2 != 0) { //if i is an odd integer
    sum = sum + i;
  }
  i++;
}
console.log(sum);
