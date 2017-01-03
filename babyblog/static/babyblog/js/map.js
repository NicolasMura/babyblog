    /*-------------------------------------------------*/
    /* =  map
    /*-------------------------------------------------*/


              
    function initialize() {
        var loc, map, marker, infobox, styles;
        
        loc = new google.maps.LatLng(51.508606, -0.133789);
        
        map = new google.maps.Map(document.getElementById("map"), {
             zoom: 17,
             center: loc,
             scrollwheel: false,
             navigationControl: false,
             mapTypeControl: false,
             scaleControl: false,
             draggable: true,
             mapTypeId: google.maps.MapTypeId.ROADMAP
        });
        
        // marker = new google.maps.Marker({
        //     map: map,
        //     position: loc,
        //     visible: true
        // });

        marker = new google.maps.Marker({
            position: new google.maps.LatLng(51.508606, -0.133789),
            map: map,
            title: 'Uluru (Ayers Rock)',
            icon: 'images/pin.png' // This path is the custom pin to be shown. Remove this line and the proceeding comma to use default pin
        });
        

        var styledMap = new google.maps.StyledMapType(styles,
          {name: "Styled Map"});

        map.mapTypes.set('map', styledMap);
        map.setMapTypeId('map'); 

        google.maps.event.addListener(marker, 'click', function() {
            infobox.open(map, this);
            map.panTo(loc);
        });
    }
    google.maps.event.addDomListener(window, 'load', initialize); 