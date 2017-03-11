//This is based on “Flexible Countdown”. The parameter names are not as helpful, but the problem is essentially identical; don’t be thrown off! Given 4 parameters (param1,param2,param3,param4), print the multiples of param1, starting at param2 and extending to param3. One exception: if a multiple is equal to param4, then skip (don’t print) that one. Do this using a WHILE loop.

//Example: Given (3,5,17,9), print 6,12,15 (which are all of the multiples of 3 between 5 and 17, except for the value 9).


function final_countdown(param1, param2, param3, param4){
  var i = param2;
  while(i <= param3){
    if (i % param1 == 0){
      if (i != param4) {
        console.log(i);
      }
    }
    i++; //increment needs to be within while loop (the last thing within while loop). 
  }
}

final_countdown(3,5,17,9);
