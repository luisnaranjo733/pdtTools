var pdtApp = angular.module("PdtApp", ['ui.router']);
pdtApp.controller("PdtCtrl", function($scope) {
    
});

pdtApp.config(function($stateProvider, $urlRouterProvider) {

    $stateProvider.state('home', {
        url: "/",
        templateUrl: "partials/home.html"
    })
})