$(document).ready(function() {
    window.setInterval(function initialize() {
        console.log("ajax call...");
        $.ajax({
            url: '/get_scooter',
            type: "GET",
            success: function (data) {
                console.log("ajax call");
                var all_scooter = []; // initialize empty list for scooters
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

                var map = new google.maps.Map(document.getElementById('map_canvas'), {
                    zoom: 10,
                    center: new google.maps.LatLng(52.711171, 13.67874),
                    mapTypeId: google.maps.MapTypeId.ROADMAP
                });
                var infowindow = new google.maps.InfoWindow();

                var marker, i;

                for (i = 0; i < all_scooter.length; i++) {
                    marker = new google.maps.Marker({
                        position: new google.maps.LatLng(all_scooter[i][0], all_scooter[i][2]),
                        map: map
                    });

                    google.maps.event.addListener(marker, 'click', (function (marker, i) {
                        return function () {
                            infowindow.setContent(all_scooter[i][1]);
                            infowindow.open(map, marker);
                        }
                    })(marker, i));
                }
            }
        })
    }, 5000);
});