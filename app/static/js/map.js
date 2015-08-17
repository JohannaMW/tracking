$(document).ready(function() {
    var map;
    var all_vehicle = [];
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

    window.setInterval(function getVehicle() {
        console.log("ajax call...");
        $.ajax({
            url: '/get_vehicle',
            type: "GET",
            success: function (data) {
                console.log("ajax call");
                all_vehicle = []; // initialize empty list for vehicles
                $.each(data, function () {
                    console.log("Data:" + data);
                    var vehicle = [];
                    $.each(this, function (k, v) {
                        console.log("k=" + k);
                        console.log("v=" + v);
                        if (k == 'fields') {
                            $.each(this, function (a, b) {
                                console.log('vehicle' + a);
                                if ((a === 'lat') || (a === 'vehicle') || (a === 'long')) {
                                    vehicle.push(b)
                                }
                                else {
                                }
                            })
                        }
                    });
                    console.log(vehicle);
                    all_vehicle.push(vehicle);
                });
                console.log("All scooter" + all_vehicle);
                setMarker(all_vehicle);
            }
        })
    }, 1000);

    function setMarker(all_vehicle) {
        console.log("in setMarker" );
        var color;
        for (i = 0; i < all_vehicle.length; i++) {
            if (all_vehicle[i][1][1] == false) {
                color = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'
            }
            else {
                color = 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
            }
            console.log("All vehicle:" + all_vehicle);
            console.log("Latitude:" + all_vehicle[i][2]);
            console.log("Longitude:" + all_vehicle[i][1]);
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(all_vehicle[i][2], all_vehicle[i][1]),
                map: map,
                icon: color
            });

            google.maps.event.addListener(marker, 'click', (function (marker, i) {
                return function () {
                    infowindow.setContent(all_vehicle[i][0]);
                    infowindow.open(map, marker);
                }
            })(marker, i));
        }
    }
    getLocation();
});
