//Create ThreesFives() that adds values from 100 and 4000000 (inclusive) if that value is evenly divisible by 3 or 5 but not both. Display the final sum in the console.

function ThreesFives(){
  var sum = 0;
  for (i = 100; i <= 400000; i++){
    if (i % 3 == 0 ^ i % 5 == 0  ){ //^ is exclusive OR
      sum += i;
    }
  }
  console.log(sum);
}

ThreesFives();

//Second: Create BetterThreesFives(start,end) that allows you to enter arbitrary start and end values for your range. Think of your above ThreesFives() function as BetterThreesFives(100,4000000).
function BetterThreesFives(start, end){
  var sum = 0;
  for (i = start; i <= end; i++){
    if (i % 3 == 0 ^ i % 5 == 0){
      sum += i;
    }
  }
  console.log(sum);
}
BetterThreesFives(100, 400000);
