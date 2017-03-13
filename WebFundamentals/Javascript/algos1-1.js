var g = null;
var h = undefined;

if (g == h){
  console.log('g==h');
} else if (g===h) {
  console.log('g===h');
} else {
  console.log('none of the above is true')
}

//ternary operator (?) -- only takes true or false
var Rob = (condition) ? true : false;
var Rob = bob > ross ? 'Boss' : 'Ross' //is bob greater than ross? if so, set Rob='Boss', otherwise Rob='Ross'

var Max = Max > temp ? Max : temp;

var bob = 4;
var ross = 12;
//nested if
//and (&&) operator
//or (||) operator
if (bob < ross && bob == 4){
  console.log('hi');
}

//for loops: you know how many times you want to do something
//while loops: you don't know how many times you want to do
//do while loops: do at least once

array = 'hello'
console.log(array.length); //5

for (var i = 0; i < array.length; i++){
  console.log(array[i]);
}

while(condition){
  do stuff;
}

var bob = 4;
var ross = 12;
while(ross > bob){
  console.log('in loop');
  bob+=1;
}
