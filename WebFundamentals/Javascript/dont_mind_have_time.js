var HOUR = 2;
var MINUTE = 10;
var PERIOD = 'PM';

//challenge
if (MINUTE < 30){
  if(PERIOD == 'AM'){
    console.log("It's just after", HOUR, 'in the morning');
  } else if (PERIOD=='PM'){
    console.log("It's just after", HOUR, 'in the evening');
  }
} else if (MINUTE >= 30) {
  if (PERIOD == 'AM'){
    console.log("It's almost", HOUR+1, 'in the morning');
  } else if (PERIOD=='PM'){
    console.log("It's almost", HOUR+1, 'in the evening');
  }
}


//
if (HOUR == 8 && MINUTE == 50 && PERIOD == 'AM'){
  console.log("It's almost 9 in the morning");
} else if (HOUR == 7 && MINUTE == 15 && PERIOD == 'PM') {
  console.log("It's just after 7 in the evening");
}
