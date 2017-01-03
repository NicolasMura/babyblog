

$(document).ready(function() {
     
    $("#slider-portfolio").owlCarousel({
     
        
        slideSpeed : 300,
        paginationSpeed : 400,
        singleItem:true
     
    });

    $(".next").on("click", function(){
		$("#slider-portfolio").trigger('owl.next');
	})
	$(".prev").on("click", function(){
		$("#slider-portfolio").trigger('owl.prev');
	})
     
});

