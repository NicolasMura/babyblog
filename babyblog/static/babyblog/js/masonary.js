
$(document).ready( function () {

	/*-------------------------------------------------*/
    /* =  Masonary
    /*-------------------------------------------------*/

	var container = document.querySelector('.masonary-box');
	var msnry = new Masonry( container, {
	  // options
	  columnWidth: 370,
	  "gutter": 30,
	  itemSelector: '.vertical-box'
	});

});
