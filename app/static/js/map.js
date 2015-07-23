$(document).ready(function() {
    var map;
    var all_scooter = [];
    var infowindow = new google.maps.InfoWindow();
    var marker, i;

    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(initialize);
        } else {
            x.innerHTML = "Geolocation is not supported by this browser.";
        }
    }

    function initialize(position) {
        map = new google.maps.Map(document.getElementById('map_canvas'), {
            zoom: 15,
            center: new google.maps.LatLng(position.coords.latitude, position.coords.longitude),
            mapTypeId: google.maps.MapTypeId.ROADMAP
        });
    }

    window.setInterval(function getScooter() {
        console.log("ajax call...");
        $.ajax({
            url: '/get_scooter',
            type: "GET",
            success: function (data) {
                console.log("ajax call");
                all_scooter = []; // initialize empty list for scooters
                $.each(data, function () {
                    console.log("Data:" + data);
                    var scooter = [];
                    $.each(this, function (k, v) {
                        console.log("k=" + k);
                        console.log("v=" + v);
                        if (k == 'fields') {
                            $.each(this, function (a, b) {
                                console.log('scooter' + a);
                                if ((a === 'lat') || (a === 'scooter') || (a === 'long')) {
                                    scooter.push(b)
                                }
                                else {
                                }
                            })
                        }
                    });
                    console.log(scooter);
                    all_scooter.push(scooter);
                });
                console.log(all_scooter);
                setMarker(all_scooter);
            }
        })
    }, 100000000);

    function setMarker(all_scooter) {
        var color;
        for (i = 0; i < all_scooter.length; i++) {
            if (all_scooter[i][1][1] == false) {
                color = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
            }
            else {
                color = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
            }
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(all_scooter[i][0], all_scooter[i][2]),
                map: map,
                icon: color
            });

            google.maps.event.addListener(marker, 'click', (function (marker, i) {
                return function () {
                    infowindow.setContent(all_scooter[i][1][0]);
                    infowindow.open(map, marker);
                }
            })(marker, i));
        }
    }
    getLocation();
});
