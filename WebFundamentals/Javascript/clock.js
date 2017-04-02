var doc = document;
var clock = doc.getElementById('clock');

console.log(clock);

clock.innerHTML = 'Yo! we doing stuff!'

cat = {
  name: 'Bob',
  age: 2,
  purr: function(){
    console.log('purrr');
  }
};

console.log(cat); //{ name: 'Bob', age: 2, purr: [Function: purr] }
cat.purr(); //purrr
console.log(cat.name); //Bob

function catMaker(){
  return {
    name: 'Bob',
    age: 2,
    purr: function(){
      console.log('purrr');
    }
  };
}

cat.purr();
bob = catMaker();
bob.purr();
