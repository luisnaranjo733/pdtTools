var pdtApp = angular.module("PdtApp", ['ui.router', 'firebase']);
pdtApp.controller("PdtCtrl", function($scope, $state, $firebaseObject) {
    var rootRef = new Firebase("https://pdttools.firebaseIO.com");
    $scope.groupPassword = $firebaseObject(rootRef.child("weakGroupPassword"));
    $scope.adminPassword = $firebaseObject(rootRef.child("weakAdminPassword"));

    $scope.signIn = function(password) {
        if (password == $scope.groupPassword.$value) {
            console.log("Group password correct");
            $state.go('housePointView');
        } else if (password == $scope.adminPassword.$value) {
            console.log("Admin password correct");
        } else {
            console.log("Auth failed");
        }
    };

});

pdtApp.config(function($stateProvider, $urlRouterProvider) {

    $stateProvider.state('signIn', {
        url: "/signIn",
        templateUrl: "partials/signIn.html"
    });

    $stateProvider.state('housePointView', {
        url: "/housePointView",
        templateUrl: "partials/points.html",
        controller: function($scope) {
            $scope.test="hello";
        }
    });

});