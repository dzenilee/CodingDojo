$(document).ready(function(){
  $('#submit').click(function(){
    var first = $('#first').val();
    var last = $('#last').val();
    var description = $('#description').val();
    var createCard = "<div id='newCard' class='card'><h1>"+first + " " + last + "</h1><p>Click here for description!</p><p id='desc' style='display: none'>" + description + "</p></div>";
    $('#newCard').append(createCard); //can also use .prepend()
    return false; //has to be placed here at the bottom
  });

  //manipulating dynamically generated content:
  $(document).on('click', '#newCard p', function(){ //doesn't work if target='#newCard'
    $('p').toggle();
  });
})
