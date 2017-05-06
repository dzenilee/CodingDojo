//1. Create function rollOne() to return a randomly selected integer between 1 and 6 (inclusive).
function rollOne(){
  return Math.floor(Math.random() * 6) + 1 //returns a number between 1 and 6 inclusive
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
  console.log('max: ', max);
  console.log('min: ', min);
}

// playStatistics();

//4. Fourth, make a copy of playStatistics and add code to make playStatistics2(), so that at the end (in addition to printing high/low rolls), it also prints the total sum of all eight rolls.

function playStatistics2(){
  var min = rollOne();
  var max = rollOne();
  var sum = 0;
  for (i = 0; i < 8; i++){
    var newRoll = rollOne();
    sum += newRoll;
    console.log(newRoll);
    if (newRoll < min){
      var min = newRoll;
    } else if (newRoll > max){
      var max = newRoll;
    }
  }
  console.log('max: ', max);
  console.log('min: ', min);
  console.log('sum: ', sum);
}

// playStatistics2();

//5. Fifth, copy playStatistics2 and add code to it to make playStatistics3(num), so that it will roll as many times as you want, instead of always doing this eight times.
function playStatistics3(num){
  var min = rollOne();
  var max = rollOne();
  var sum = 0;
  for (i = 0; i < num; i++){
    var newRoll = rollOne();
    sum += newRoll;
    console.log(newRoll);
    if (newRoll < min){
      var min = newRoll;
    } else if (newRoll > max){
      var max = newRoll;
    }
  }
  console.log('max: ', max);
  console.log('min: ', min);
  console.log('sum: ', sum);
}

// playStatistics3(4);

//6. Finally, make a copy of playStatistics3 and change it to create playStatistics4(num), so that at the end instead of the total sum, it prints the average roll.
function playStatistics4(num){
  var min = rollOne();
  var max = rollOne();
  var sum = 0;
  console.log('***', min, max);
  for (i = 0; i < num; i++){
    var newRoll = rollOne();
    sum += newRoll;
    console.log(newRoll);
    if (newRoll < min){
      var min = newRoll;
    } else if (newRoll > max){
      var max = newRoll;
    }
  }
  console.log('max: ', max);
  console.log('min: ', min);
  console.log('sum: ', sum);
  console.log('average: ', sum/num);
}

playStatistics4(4);
