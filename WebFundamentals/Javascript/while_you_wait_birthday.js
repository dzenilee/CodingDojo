//Create a birthday countown.
var daysUntilMyBirthday = 60;

// For every day, print how many days left.
// If it's more than 30 days, print a sad message.
// If it's less than 30 days, print a message sound excited!
// If it's less than 5 days, SCREAM IT!
// ONCE IT'S YOUR BIRTHDAY HAVE PARTY!

while (daysUntilMyBirthday > 0 ){
  if (daysUntilMyBirthday > 30){
    console.log(daysUntilMyBirthday, "days until my brithday. Such a long time... :(");
    daysUntilMyBirthday--;
  } if (daysUntilMyBirthday<=30){
    if (daysUntilMyBirthday<=5){
      console.log(daysUntilMyBirthday, "DAYS UNTIL MY BIRTHDAY!!");
      daysUntilMyBirthday--;
    } else {
      console.log(daysUntilMyBirthday, "days until my brithday. Almost there!");
      daysUntilMyBirthday--;
    }
  }
}
