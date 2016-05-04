var pdtApp = angular.module("PdtApp", ['ui.router']);
pdtApp.controller("PdtCtrl", ["$state", function($scope, $state) {
    // function to submit the form after all validation has occurred            
    $scope.signIn = function(password) {
        if (password == "drake1848") {
            console.log("pawn");
            //$state.go("main-ui");
        } else if (password == "morrison1848") {
            console.log("admin");
            //$state.go("main-ui");
        } else {
            console.log("unauthorized");
        }
    };
}]);

pdtApp.config(function($stateProvider, $urlRouterProvider) {

    $stateProvider.state('home', {
        url: "/",
        templateUrl: "partials/home.html"
    })


    $stateProvider.state('main-ui', {
        url: "/points",
        templateUrl: "partials/points.html"
    })
})