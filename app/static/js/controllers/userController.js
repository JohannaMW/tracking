function userController($scope, $http, $routeParams, $location) {
    var userId = $routeParams.id;

    $http.get('/driver/' + userId + '').
        success(function (data) {
            $scope.driver = data;
            console.log(data);
        }).error(function (data) {
            console.log("didn't work");
            console.log(data);
        });
}