//From Star Art, derive the following that will accept and draw the given characters, not just asterisks:
// drawLeftChars(num, char)
// drawRightChars(num, char)
// drawCenterChar(num, char)
// For all three of these, you can safely assume that 'char' is a string with length 1.

var string = "";

function drawLeftChars(num, char){
  for (var i = 1; i <= num; i++){
    string += char;
  }
  console.log(string);
}

// drawLeftChars(60, '*');


function drawRightChars(num, char){
  var remaining = 75 - num;
  for (var i = 1; i <= remaining; i++){
    string += '-';
  }
  for (var j = 1; j <= num; j++){
    string += char;
  }
  console.log(string);
}

// drawRightChars(20, '^');

function drawCenterChar(num, char){
  var remaining = 75 - num;
  var left = Math.floor(remaining/2);
  var right = Math.floor(remaining/2);
  for (var l = 1; l <= left; l++){
    string += '-';
  }
  for (var i = 1; i <= num; i++){
    string += char;
  }
  for (var r = 1; r <= right; r++){
    string += '-';
  }
  console.log(string);
}

drawCenterChar(30, '@');
