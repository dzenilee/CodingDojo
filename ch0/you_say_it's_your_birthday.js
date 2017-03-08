//If 2 given numbers represent your birth month and day in either order, log "How did you know?", else log "Just another day....",
function yourBirthday(num1, num2) {
  if (num1==8 & num2==18 | num1==18 & num2==8){
    console.log("How did you know?");
  }
  else {
    console.log("Just another day....")
  }
}

yourBirthday(8,3);
yourBirthday(8,18);
yourBirthday(18,8);
