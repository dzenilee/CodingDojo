//Given two numbers, return array of length num1 with each value num2. Print "Jinx!" if they are same.

var new_array = [];
function lx_value(num1, num2){ //2, 4,
  if (num1 == num2){
    console.log("Jinx!");
  } else {
    for (var i = 0; i < num1; i++){
      new_array.push(num2)
    }
    console.log(new_array);
  }
}

lx_value(4, 23);
//lx_value(22, 22);
