
(function($) {
    "use strict";

    /*-------------------------------------------------*/
    /* =  Preloader
    /*-------------------------------------------------*/
    $(window).on('load', function() {
        $("#preloader").fadeOut("xslow");
    });

    /*-------------------------------------------------*/
    /* =  DOCUMENT READY
    /*-------------------------------------------------*/

    $(document).ready( function () {

        /*-------------------------------------------------*/
        /* =  INIT WATERMARK
        /*-------------------------------------------------*/
        function initWatermark() {
            $.watermark.options = {
              className: 'input--placeholder',
              useNative: false
            };
            //INPUT PLACEHOLDER
            $("[placeholder]").each(function() {
                $(this).watermark($(this).attr("placeholder"));
            });
            $("[type=password]").blur();
        }

        /*-------------------------------------------------*/
        /* =  scroll box show
        /*-------------------------------------------------*/
        window.sr = new scrollReveal();

        var window_height = $(window).height() ;
        $('.slide-widget ').css('height', window_height );
        $(".content-widget").mCustomScrollbar();
        $('textarea').autosize();
        $( ".datepicker" ).datepicker();

        /*-------------------------------------------------*/
        /* =  add class on header
        /*-------------------------------------------------*/
        $(window).on("scroll", function() {    
            var scroll = $(window).scrollTop();
            if (scroll >= 10) {
                $("header").addClass("change");
            }else {
                $("header").removeClass("change");
            }
        });

        /*-------------------------------------------------*/
        /* =  section-header opacity
        /*-------------------------------------------------*/
        var fadeStart=0 // 100px scroll or less will equiv to 1 opacity
        ,fadeUntil=110 // 200px scroll or more will equiv to 0 opacity
        ,fading = $('.section-header ');

        $(window).on('scroll', function(){
            var offset = $(document).scrollTop()
                ,opacity=0
            ;
            if( offset<=fadeStart ){
                opacity=1;
            }else if( offset<=fadeUntil ){
                opacity=1-offset/fadeUntil;
            }
            fading.css('opacity',opacity);
        });

        //detect iOS
        var ua = navigator.userAgent.toLowerCase();
          function removeSpaces(ua) {
            return ua.split(' ').join('');
          }
        ua = removeSpaces(ua);
        var iOS = ua.match(/(iphone|ipod|ipad)/);
          if(iOS) {
            $('html').addClass('iOS');
          }

        // initialize autosize script 

        //sticky footer trick
        var bumpIt = function() {
              $('body').css('margin-bottom', $('.footer-main').outerHeight());
            },
            didResize = false;

        bumpIt();

        //detect window resize
        $(window).on('resize', function() {
          //put scripts inside
        }).trigger('resize');

        //detect page scroll
        $(window).on('scroll', function() {
          //put scripts inside
        }).trigger('scroll');

        //INIT WATERMARK
        initWatermark();

        /*-------------------------------------------------*/
        /* =  scroll
        /*-------------------------------------------------*/
        if ($(window).width() <= 768) { 
          $("header nav").mCustomScrollbar(); 
        } else {
          $("header nav").mCustomScrollbar("destroy");
        }

        /*-------------------------------------------------*/
        /* =  ON RESIZE
        /*-------------------------------------------------*/
        $(window).on('resize', function() {
          var screen_size = $(window).width();
          if (screen_size <= 768) {
            $("header nav").mCustomScrollbar();
          }
          else {
            $("header nav").mCustomScrollbar("destroy");
          }
        }).trigger('resize');

        /*-------------------------------------------------*/
        /* =  open sidebar
        /*-------------------------------------------------*/
        $('#open-sidebar').on("click", function(){
            $('.widget-wrap').toggleClass('active');
        });
        
        $('.close-sidebar').on("click", function(){
            $(this).parent().parent('.widget-wrap').toggleClass('active');
        });
        $('.widget-bgr').on("click", function(){
            $(this).parent().toggleClass('active');
        });

        /*-------------------------------------------------*/
        /* =  open contact popup
        /*-------------------------------------------------*/
        $('#open-contact').on("click", function(){
            $('.contact-wrap').toggleClass('active');
        });
        $('.close-contact').on("click", function(){
            $(this).parent().parent('.contact-wrap').toggleClass('active');
        });
        $('.contact-bgr').on("click", function(){
            $(this).parent().toggleClass('active');
        });

        /*-------------------------------------------------*/
        /* =  Responsive navigation
        /*-------------------------------------------------*/
        $('#open-nav').on("click", function(){
            $('nav').toggleClass('active');
        });
        $('nav a').on("click", function(){
            $('nav').removeClass('active');
        });

        /*-------------------------------------------------*/
        /* =  Generate random number for form check
        /*-------------------------------------------------*/
        var generateRandom = function(element) {
            var word = ['one', 'two', 'three', 'four', 'five'];
            var rand = (Math.floor(Math.random() * 4));
            var correct = word[rand];
            $(element).html(correct);
            return correct;
        }        

        var correct = generateRandom('.test p span');

        /*-------------------------------------------------*/
        /* =  Highlighting checked radio button 
        /*-------------------------------------------------*/         
        $('input[name=rand]').on('click', function() {
            $('input[name=rand]').parent().removeClass('active1');
            $('input[name=rand]:checked').parent().addClass('active1');
        });

        /*-------------------------------------------------*/
        /* =  Popup notification 
        /*-------------------------------------------------*/ 
        var showNotification = function(message, className) {
            $('.popup-email').fadeIn('fast');
            $('.element p').remove();
            $('.element').prepend('<p class="' + className + '">' + message + '</p>');
        }

        var closeNotification = function(element) {
            $(element).fadeOut('fast');
        }

        $('#btn').on('click', function() {
            closeNotification('.popup-email');
        });

        /*-------------------------------------------------*/
        /* =  Form validation
        /*-------------------------------------------------*/

         $('.contact-form').validate({
            errorElement: 'p',
            errorClass: 'notify',
            rules: {
                name: "required",
                subject: "required",
                mail: {required: true, email: true},
                message: "required"
            },
            submitHandler: function(form) {               
                if($('input[name=rand]:checked').val() === correct) {                
                    $.post('form_data.php', $(form).serialize(), function(response) {
                        $(form)[0].reset();
                        correct = generateRandom('#test p span');
                        closeNotification('.contact-wrap');
                        showNotification(response.msg, response.class);
                    }, 'json');
                } else showNotification('Incorrect number selected!', 'error');              
                
            }
        }); 

    });

})(jQuery);