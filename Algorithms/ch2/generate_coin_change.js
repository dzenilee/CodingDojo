//Change is inevitable (especially when you break a twenty!). Make generateCoinChange(cents). Accept a number of American cents, compute and print how to represent that amount with the smallest number of coins possible. Common American coins are penny (1 cent), nickel (5 cents), dime (10 cents) and quarter (25 cents).

function generateCoinChange(cents){
  var remaining = cents;
  var coin_count = 0;
  while (remaining > 0){
    for (var coin = 25; coin >= 1; coin--){
      if (coin == 25 | coin == 10 | coin == 5 | coin == 1){
        coin_count = Math.floor(remaining/coin);
        remaining = remaining % coin;
        console.log(coin_count);
      }
    }
  }
}

generateCoinChange(94); // 3 1 1 4 (might want to try again with coin type appearing)
