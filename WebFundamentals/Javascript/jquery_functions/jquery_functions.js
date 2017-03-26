$(document).ready(function(){
  $('#addClass_btn').click(function(){
    $('#addClass_demo').addClass("red");
  })

  $('#slideToggle_btn').click(function(){
    $('#joy_sadness').slideToggle("slow");
  })

  $('#append_btn').click(function(){
    $('#append_to').append(" I'm a new paragraph! Kinda!");
  })

  $('#fadeOut_btn').click(function(){
    $('#fadeMeOut').fadeOut("slow");
  })

  $('#val_btn').click(function(){
    var value = $("#single").val();
    $('#val_p').html('<b>first option: </b>' + value);
  })

  $('#show_btn').click(function(){
    $('#rest').show("slow");
  })

  $('#before_btn').click(function(){
    $('#beforeMe').before(["Hello", "World", "!"]);
  })

  $('#data_btn').click(function(){
    $('#target').data("test", {first: "Joy", last: "Disgust"});
    $('li:first').text($('#target').data("test").first);
    $('li:last').text($('#target').data("test").last);
  })
});
