//1. Create function rollOne() to return a randomly selected integer between 1 and 6 (inclusive).
function rollOne(){
  return Math.floor(Math.random() * 6) + 1 //returns a number between 1 and 7
}

// console.log(rollOne());

//2. Second, create a function playFives(num), which should call rollOne() multiple times – 'num' times, in fact, where 'num' is input parameter to playFives(num). Each time, it should print the value rollOne() returns, and if that return value is 5, also print “That’s good luck!”
function playFives(num){
  for (i = 0; i < num; i++){
    var result = rollOne();
    console.log(result);
    if (result == 5){
      console.log("That's good luck!");
    }
  }
}

// playFives(3);


//3. Third, create a new function named playStatistics(), which should call rollOne() eight times (but not print anything after each call). After the last of these eight calls, it should print out the lowest and highest values that it received from rollOne, among those eight calls.

function playStatistics(){
  var min = rollOne();
  var max = rollOne();
  for (i = 0; i < 8; i++){
    var newRoll = rollOne();
    console.log(newRoll);
    if (newRoll < min){
      var min = newRoll;
    } else if (newRoll > max){
      var max = newRoll;
    }
  }

}

playStatistics()
