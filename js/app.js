
var pdtApp = angular.module("PdtApp", ['ui.router', 'firebase']);

pdtApp.controller("LogInCtrl", function($scope, $state, $firebaseObject, $rootScope, AuthService) {
    var rootRef = new Firebase("https://pdttools.firebaseIO.com");
    $scope.groupPassword = $firebaseObject(rootRef.child("weakGroupPassword"));
    $scope.adminPassword = $firebaseObject(rootRef.child("weakAdminPassword"));

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

pdtApp.controller("housePointMasterCtrl", function($scope, $rootScope) {
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

pdtApp.controller("housePointWeeksCtrl", function($scope) {

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
        url: "/weeks",
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

