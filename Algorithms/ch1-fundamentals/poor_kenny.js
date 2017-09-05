/*
Kenny tries to stay safe, but somehow everyday something happens.
If there is a 10% chance of volcano, 15% chance of tsunami,
20% chance of earthquake, 25% chance of blizzard, and 30% chance of meteor strike,
write function whatHappensToday() to print the outcome.
*/

//The instructions are difficult to understand. 

function whatHappensToday(){
  var chance = .8;
  if (chance <= .1){
    console.log("Volcano!");
  } else if (chance <= .15){
    console.log("Tsunami!");
  } else if (chance <= .2){
    console.log("Earthquake!");
  } else if (chance <= .25){
    console.log("Blizzard!");
  } else if (chance <= .3){
    console.log("Meteor strike!");
  }
}

whatHappensToday();
