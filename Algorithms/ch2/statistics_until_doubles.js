//Here’s another game for our New Year’s Eve party. Implement a ’20-sided die’ that randomly returns integers between 1 and 20 inclusive. Roll these, tracking statistics until you get a value twice in a row. Display number of rolls, min, max, and average.

//still working 
function rollOne(){
  return Math.floor(Math.random() * 20) + 1 //returns a number between 1 and 20 inclusive
}

function die_stats(){
  var roll = rollOne();
  // var max = rollOne();

  //roll a 20-sided die
  while (rollOne() != prev_roll){
    //keep rolling
    rollOne();
    if
  }
  console.log('number of rolls: ', count);
  console.log('min: ', min);
  console.log('max: ', max);
  console.log('average: ', average);
}

die_stats();
