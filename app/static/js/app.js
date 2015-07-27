var scooter_ang = angular.module('scooter_ang', ['ngRoute', 'ngCookies']);

scooter_ang.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {templateUrl: '/static/js/views/home.html', controller: homeController }).
        when('/profile/:id', {templateUrl: '/static/js/views/profile.html', controller: userController }).
        otherwise({redirectTo: '/'});
}]);