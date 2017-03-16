// Primitive data types:
// * Strings
// * numbers
// * undefined (absence of types), null

console.log(x)
var x;
x = 3;
//
console.log(null == undefined) //true
console.log(null === undefined) //false

//Complex data types:
//* Arrys: ordered collections of data

var x = [1, 2, 'bob', 'rob', true];
console.log(x);

var y = x+[3, 5, 'jenny']
console.log(y); //1,2,bob,rob,true3,5,jenny

var a = [3, 5]
var b = [4, 6]
console.log(a+b)

a[6] = 30; //

console.log(a); [ 3, 5, , , , , 30 ]
console.log(a.length); //7

//Objects (like arrays in that they're collections, but objects use keys to return values.)

var x = {
  'bob': 'Ross',
  'rob': 'Ross'
};

//console.log(x['bob']);
console.log(x.bob); //Ross
console.log(x['b'+'o'+'b']) //Ross

x['alan'] = 'teacher'; //add 'teacher' key
console.log(x)

//Objects are unordered.

for (var key in x){
  console.log(key);
} //returns the keys bob, rob, alan one line at a time.

//Object Oriented Language: associative name
//rely on objects that interact with each toerh
//cf. procedural where you're feeding

//Mathematical operators
console.log(9%3); //0

// = assignment operator (on the right gets evaluated first, then gets assigned to thing on the left)

// * Statement: describes something
// var x = 7; <-- is a statement (typically it has a ; at the end)
// * Expression: evaluates and produces value
// var x = 7 + 8; (7 + 8) is an expression (the whole thing though is a statement)
//
// square brackets contain expressions.

// Logical comparison:
// Equality
console.log(4 == '4'); //loosely equivalent, so TRUE
console.log(4 === '4'); //strictly equivalent, so FALSE

//Ineqaulity (!=)
console.log(4 != '4');  //false
console.log(4 !== '4');  //true

//Conditional
console.log(4 <= 5);

//AND
console.log(4 <= 5 && 6 <= 7);//true
console.log(4 <= 5 && 8 <= 7);//false

//OR
console.log(4 <= 5 || 8 <= 7);//true

var x = [1, 2, 3, 4, 5]
console.log(x);

function changer(arr){
  arr = 'bob';
}

changer(x); //all you're doing is passing in a location in memory. You haven't changed the piece of memory referenced by arr.


function changer(arr){
  console.log(arr);
  arr = 'bob';
  console.log(arr);
}

changer(x); //bob \ [1, 2, 3, 4, 5] \ bob

//Conditionals

//Use a switch statement if you have more than three if's.
console.log(false == 1-1); //true
console.log(false === 1-1); //false


//Loops
1. for loops (known number of loops)
2. while loops (unknown # of loops)
3. do while loops
4. for in loops

for (var i = 0; i <array.length; i++){
  console.log(i);
} //i++ is executed at the end of block.

// All three are optional parameters.
// e.g., You can have i++ inside the {}.

for (var i=0; ; ){
  if (i>10){
    break;  //or return
  }
  console.log(i);
  i++;
}

//when you want to do something at least one time but not sure how many. Used very rarely.
do{
  console.log('hi')
}while(false); //will print 'hi' (once) even if condition not true.

//for in loops
for (var i in something){

}

//Store function in a variable!
var x = function(){
  console.log('hi');
}

function bob(f){
  f(); //pass a function in as a parameter
}

bob(function(){console.log('hi')}); //hi

bob('bob');
}); //'not a function!'

var x = {
  f1: function(){
    console.log('hola');
  },
  f2: function(){
    console.log('hellow');
  },
  f3: function(callback){
    if (callback instanceof Function){
      callback();
    } else{
      console.log("ERROR");
    }
  }
}

x.f1();
x.f2();
x.f3(function(){console.log('I can spell hello')})
