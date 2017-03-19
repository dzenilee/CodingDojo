//Part I
// var students = [
//   {first_name:  'Michael', last_name : 'Jordan'},
//   {first_name : 'John', last_name : 'Rosales'},
//   {first_name : 'Mark', last_name : 'Guillen'},
//   {first_name : 'KB', last_name : 'Tonel'}
// ]
//
// for (var i = 0; i < students.length; i++){
//   console.log(students[i].first_name, students[i].last_name);
// }

//Part II (Optional)
var users = {
  'Students': [ //i=0
    {first_name:  'Michael', last_name : 'Jordan'}, //Students[0]
    {first_name : 'John', last_name : 'Rosales'}, //Students[1]
    {first_name : 'Mark', last_name : 'Guillen'}, //Students[2]
    {first_name : 'KB', last_name : 'Tonel'}
  ],
  'Instructors': [ //i=1
    {first_name : 'Michael', last_name : 'Choi'},
    {first_name : 'Martin', last_name : 'Puryear'}
  ]
}

// console.log(Object.keys(users)); //['Students', 'Instructors']

function doStuff(obj){
  // get keys of input object
  var keys = Object.keys(obj) //stores obj's keys in list form

  // use keys to get array of people names
  for (var i = 0; i < keys.length; i++){ //iterate keys, a list of keys in obj: ['Students', 'Instructors']
  var curKey = keys[i]; //store each item in keys, a list, in curKey
  console.log(curKey + ':'); //prints each item in curKey, line by line: Students \n Instructors
  var peepList = obj[curKey]; //= obj['Students', 'Instructors']
  // console.log(peepList); //returns names list for Students and for Instructors
  // iterate the array to get student objects
  for (var j = 0; j < peepList.length; j++){
      var peep = peepList[j];
      for (var char_first = 0; char_first < peep.first_name.length; char_first++){ //count number of characters in first name
        char_first;
      }
      for (var char_last = 0; char_last < peep.last_name.length; char_last++){ //count number of characters in first name
        char_last;
      }
      //print the student's information
      console.log('  ' + peep.first_name + ' ' + peep.last_name + ' ' + (char_first+char_last));
    }
  }


}

doStuff(users);
//Returns:
// Students:
//   Michael Jordan 13
//   John Rosales 11
//   Mark Guillen 11
//   KB Tonel 7
// Instructors:
//   Michael Choi 11
//   Martin Puryear 13
// [Finished in 0.171s]
