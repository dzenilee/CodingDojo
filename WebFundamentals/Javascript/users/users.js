$(document).ready(function(){
  $('button').click(function(){
    var first = $('#first_name').val();
    var last = $('#last_name').val();
    var email = $('#email').val();
    var contact = $('#contact').val();
    $('tbody').append('<tr><td>' + first + '</td><td>' + last + '</td><td>' + email + '</td><td>' + contact + '</td></tr>');
    return false;
  });
}); 
