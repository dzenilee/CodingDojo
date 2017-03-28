$(document).ready(function(){
  //get info from form submission
  $('#submit').click(function(){
    var first = $('#first').val(); //or $('input[name=first]').val() if using ('form').submit
    var last = $('#last').val();
    var description = $('#description').val();
    var createCard = "<div class='card'><h1>" + first + " " + last + "</h1><p>Click here for description!</p><p id='desc' style='display: none'>" + description + "</p></div>";
    $('#newCard').append(createCard); //can also use .prepend()
    return false; //has to be placed here at the bottom
  });

  //manipulate static cards
  $(document).on('click','.card h1+p', function(){ //h1+p: selects all <p> elements that are placed immediately after <h1> elements
    $(this).toggle();
    $(this).next().toggle();

  })

  //manipulate dynamically generated content
  $(document).on('click', '#newCard.children(h1+p)', function(){
    // $(this).toggle();
    $(this).next().toggle();
  });

//This is for later:
  //create contact card that would display my (github) information
  // $('form[class=trb]').submit(function(e){
  //   e.preventDefault();
  //   var gitUserName = $('input[name=gituser]').val();
  //   var gitUrl = 'https://api.github.com/users/octocat/orgs'; //from https://developer.github.com/v3/
  //   $.get(gitUrl + gitUserName, function(results){
  //     console.log(results);
  //     var newPeep = {};
  //     newPeep.first = results.name.split(' ')[0];
  //     newPeep.last = results.name.split(' ')[1];
  //     newPeep.description = results.bio;
  //     gitCard(newPeep);
  //   }, 'json');
  // })

  // function gitCard(object){
  //   var gitCard = "<div class='card'><h1>" + object.first + " " + object.last + "</h1><p>Click here for description!</p><p id='desc' style='display: none'>" + object.description + "</p></div>";
  // }

})
