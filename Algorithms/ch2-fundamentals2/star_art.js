//Assume that you have a text field that is exactly 75 characters long. You want to fill it with spaces and asterisks ('*'), sometimes called stars. You should print the given number of asterisks consecutively. Depending on which function is called, those stars should be left-justified (the first star would be very first character in the text field), or right-justified (last star would be very last character in the text field, with potentially some number of spaces at the beginning of the text field before the block of stars start), or centered in the 75 -character text field (with the same number of spaces on either side of the block of stars, plus/minus one).



//Write a function drawLeftStars(num) that accepts a number and prints that many asterisks
function drawLeftStars(num){
var star_string = "";
  for (var i = 1; i <= num; i++){
    star_string += '*';
  } console.log(star_string);
}

drawLeftStars(3);

//Write a function drawRightStars(num) that prints 75 characters total. The stars should build from the right side. the last num characters should be asterisks; the other remaining of the 75 should be spaces.
function drawRightStars(num){
  var string = "";
  var remaining = 75 - num;
  for (var i = 1; i <= remaining; i++){
    string += '-';
  }
  for (var j = 1; j <= num; j++){
    string += '*';
  }
  console.log(string);
}

drawRightStars(60);

//Write a function drawCenterStars(num) that prints 75 characters total. The stars should be centered in the 75. the middle num characters should be asterisks; the rest of the 75 characters should be spaces.
function drawCenterStars(num){
  var string = "";
  var remaining = 75 - num;
  var left = Math.floor(remaining/2);
  var right = Math.floor(remaining/2);
  for (var h = 1; h <= left; h++){
    string += '-';
  }
  for (var i = 1; i < num; i++){
    string += '*';
  }
  for (var j = 1; j <= right; j++){
    string += '-';
  }
  console.log(string);
}

drawCenterStars(60);
