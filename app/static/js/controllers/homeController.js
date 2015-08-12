function homeController($scope, $http ) {
    $http.get('/scooter/').
        success(function (data) {
            $scope.vehicles = data;
            console.log(data);
        }).error(function (data) {
            console.log("didn't work");
            console.log(data);
        });

}