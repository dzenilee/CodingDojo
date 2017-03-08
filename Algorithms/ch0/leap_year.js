// Write a function that determines whether a given year is a leap year.
// If a year is divisible by four, it is a leap year, unless it is divisible by 100.
// However, if it is divisible by 400, then it is.

function leapyearOrNot(year){
  if (year % 4 == 0){
    if (year % 100 == 0){
        console.log(year+" is not a leap year.")
      } else {
        console.log(year+ " is a leap year.")
      }
    } else {
    console.log(year+" is not a leap year.")
  }
}

leapyearOrNot(2002);
leapyearOrNot(1916);
leapyearOrNot(2017);
