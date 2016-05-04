
var pdtApp = angular.module("PdtApp", ['ui.router']);

pdtApp.controller("LogInCtrl", function($scope, $state) {
    var rootRef = new Firebase("https://pdttools.firebaseIO.com");
    $scope.groupPassword = $firebaseObject(rootRef.child("weakGroupPassword"));
    $scope.adminPassword = $firebaseObject(rootRef.child("weakAdminPassword"));

    $scope.logIn = function(password) {
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
