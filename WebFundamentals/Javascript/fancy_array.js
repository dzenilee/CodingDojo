// Normally, if you print an array such as ["James", "Jill", "Jane", "Jack"], you will see the following:
//
// [ "James", "Jill", "Jane", "Jack" ]
//
// Let's make it look fancy! Write a function that will make it print like:
//
// 0 -> James
// 1 -> Jill
// 2 -> Jane
// 3 -> Jack

function fancy(array){
  for (var i = 0; i < array.length; i++){
    console.log(i + " -> " + array[i]);
  }
}

var arr = [ "James", "Jill", "Jane", "Jack" ]

fancy(arr);
