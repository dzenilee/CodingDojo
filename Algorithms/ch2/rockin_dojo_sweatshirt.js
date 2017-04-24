/*
Ever since you arrived at the Dojo, you wanted one of those cool Coding Dojo sweatshirts - maybe even more than one. Let's say they cost $20 (including tax), but friendly Josh will give a 9% discount if you buy two, or a nice 19% discount if you buy three, or a sweet 35% discount if you buy four or more. He only accepts cash and doesn't have coins, so you have to round up to the nearest dollar. Build a function sweatshirtPricing(num) that, given how many sweatshirts you want, returns the cost.
*/

function sweatshirtPricing(num){
  var cost;
  if (num == 1){
    cost = 20;
  } else if (num == 2){
    cost = 20 * num * (1-.09);
  } else if (num == 3){
    cost = 20 * num * (1-.19);
  } else if (num >= 4){
    cost = 20 * num * (1-.35);
  }
  return Math.ceil(cost); //49
  // return Math.trunc(cost); //48
  // return Math.floor(cost); //48
}

console.log(sweatshirtPricing(3));
