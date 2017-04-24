

$(document).ready(function() {

$("#dragonfly-hide").hide();
$("#wtc-hide").hide();
$("#party-hide").hide();


        $('#home-dragonfly').hover(function(e){
            e.preventDefault();
          $('.dragonfly-hover').stop().fadeOut(300, function(){
            $('#dragonfly-hide').stop().fadeIn(300);
          })
        }, function(){
            $('#dragonfly-hide').stop().fadeOut(300, function(){
              $('.dragonfly-hover').stop().fadeIn(300);
            })
        });

        $('#home-wtc').hover(function(){
          $('#wtc-hover').stop().fadeOut(300, function(){
            $('#wtc-hide').stop().fadeIn(300);
          })
        }, function(){
            $('#wtc-hide').stop().fadeOut(300, function(){
              $('#wtc-hover').stop().fadeIn(300);
            })
        });

        $('#home-party').hover(function(){
          $('#party-hover').stop().fadeOut(300, function(){
            $('#party-hide').stop().fadeIn(300);
          })
        }, function(){
            $('#party-hide').stop().fadeOut(300, function(){
              $('#party-hover').stop().fadeIn(300);
            })
        });




});
