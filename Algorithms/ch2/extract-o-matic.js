/*
Create the extractDigit(num,digitNum) function that given a number and a digit number, returns the numeral value of that digit. 0 represents the ones digit, 1 represents the tens digit, etc. Given (1824,2), return 8. Given (1824,0), return 4. Given (1824,7), return 0.

Second: handle negative digitNum values, where -1 represents tenths digit (0.x), -2 represents hundredths digit (0.0x), etc. Given (123.45,-1), return 4.

Third: handle negative num values as well, doing what you think is appropriate.
*/

// still working on 2nd and 3rd 
function extractDigit(num, digitNum){
  num = num + ""; //same as str = String(num)
  var numIntoArray = num.split("")
  // console.log(numIntoArray); // ["1", "8", "2", "0"]
  numIntoArray.reverse();
  // console.log(numIntoArray); // [ '0', '2', '8', '1' ]
  var joined = numIntoArray.join("");
  // console.log(joined); //0281
  // console.log(typeof(joined)); //string
  if (digitNum > num.length){
    return 'Index out of range'
  } else {
    return joined[digitNum];
  }
}

console.log(extractDigit(1820, 0));
console.log(extractDigit(1824, 7));
