var vehicle_ang = angular.module('vehicle_ang', ['ngRoute', 'ngCookies']);

vehicle_ang.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {templateUrl: '/static/js/views/home.html', controller: homeController }).
        when('/profile/:id', {templateUrl: '/static/js/views/profile.html', controller: userController }).
        otherwise({redirectTo: '/'});
}]);