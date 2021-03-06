
var pdtApp = angular.module("PdtApp", ['ui.router', 'firebase']);
var firebaseURL = "https://pdttools.firebaseIO.com";

pdtApp.controller("LogInCtrl", function($scope, $state, $firebaseObject, $rootScope, AuthService) {
    var ref = new Firebase(firebaseURL);
    $scope.groupPassword = $firebaseObject(ref.child("weakGroupPassword"));
    $scope.adminPassword = $firebaseObject(ref.child("weakAdminPassword"));

    $scope.logIn = function(password) {
        if (password == $scope.groupPassword.$value) {
            console.log("Group password correct");
            AuthService.logIn();
            $state.go('housePointMaster');
        } else if (password == $scope.adminPassword.$value) {
            console.log("Admin password correct");
        } else {
            console.log("Auth failed");
        }
    };
});

pdtApp.controller("housePointMasterCtrl", function($scope, $firebaseArray) {

    var ref = new Firebase(firebaseURL + "/users");
    $scope.data = new $firebaseArray(ref);

    $scope.people = [
        {
            name: "Luis Naranjo",
            points: 42,
        },
        {
            name: "Nick Polsin",
            points: 36
        }
    ];
});

pdtApp.controller("housePointWeeksCtrl", function($scope, $stateParams) {
    // use this url parameter to query this person's records in the firebase and load their data onto scope
    // using their name as the logical equivalent to their PK
    // probably can find a better way to do this (maybe with firebase uuid)
    $scope.name = $stateParams.name
});


pdtApp.factory('AuthService', function() {
    var authService = {};

    authService.logIn = function() {
        console.log("Logging in");
        localStorage.setItem("pdtToolsAuth", "true");
    }

    authService.logOut = function() {
        console.log("Logging out");
        localStorage.setItem("pdtToolsAuth", "false");
    }

    authService.isAuthenticated = function() {
        var authenticated = localStorage.getItem("pdtToolsAuth") == "true";
        if (authenticated) {
            console.log("user IS logged in");
        } else {
            console.log("user IS NOT logged in");
        }
        return authenticated;
    }

    return authService;
});



pdtApp.config(function($stateProvider, $urlRouterProvider) {
    $stateProvider.state('logIn', {
        url: "/logIn",
        templateUrl: "partials/login.html",
        controller: "LogInCtrl",
        authenticate: false
    });


    $stateProvider.state('housePointMaster', {
        url: "/",
        templateUrl: "partials/housePointMaster.html",
        controller: 'housePointMasterCtrl',
        authenticate: true
    });

    $stateProvider.state('housePointWeeks', {
        url: "/points/{name}",
        templateUrl: "partials/housePointWeeks.html",
        controller: "housePointWeeksCtrl",
        authenticate: true
    });

    $urlRouterProvider.otherwise("logIn");
})
.run(function ($rootScope, $state, AuthService) {
    $rootScope.$on("$stateChangeStart", function(event, toState, toParams, fromState, fromParams){
        if (toState.authenticate && !AuthService.isAuthenticated()){
            // User isn’t authenticated
            $state.transitionTo("logIn");
            event.preventDefault(); 
        }
    });
});

