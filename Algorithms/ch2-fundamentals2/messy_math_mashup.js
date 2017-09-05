//not done. 

function messyMath(num){
  var sum = 0;
  for (var count = 0; count <= num; count++){

    if (count % 3 != 0){
      if (count % 7 == 0){
        sum += count * 2;
      }
      sum += count;
    }
    if (count == 1/3 * num){
      console.log(-1);
    }
  }
console.log(sum);
}

messyMath(4);
messyMath(8);
messyMath(15);
