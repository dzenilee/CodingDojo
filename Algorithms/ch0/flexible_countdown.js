//Based on earlier “Countdown By Fours”, given lowNum, highNum, mult,
// print multiples of mult from highNum down to lowNum, using a FOR loop.

function flexible_countdown(lowNum, highNum, mult){
  for (var i = highNum; i >= lowNum; i--) {
    if (i%mult == 0){
      console.log(i);
    }
  }
}

flexible_countdown(2,9,3);
