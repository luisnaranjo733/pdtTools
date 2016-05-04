var pdtApp = angular.module("PdtApp", ['ui.router']);

pdtApp.controller("LogInCtrl", function($scope, $state) {
    $scope.logIn = function(password) {
        console.log(password);
    }
});


pdtApp.controller("housePointsCtrl", [function($scope) {


}]);

pdtApp.config(function($stateProvider, $urlRouterProvider) {
    //$urlRouterProvider.otherwise("/login");
    $stateProvider.state('logIn', {
        url: "/",
        templateUrl: "partials/login.html",
        controller: "LogInCtrl"
    })


    $stateProvider.state('pointsView', {
        url: "/points",
        templateUrl: "partials/points.html",
        controller: "housePointsCtrl"
    })
})