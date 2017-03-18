//Part I
var students = [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]

for (var i = 0; i < students.length; i++){
  console.log(students[i].first_name, students[i].last_name);
}

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

//Not complete: working 
console.log(users.Students);
console.log(users.Students[2]); //{first_name : 'Mark', last_name : 'Guillen'},
console.log(users.Students[2].first_name); //Mark
