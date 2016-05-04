
var pdtApp = angular.module("PdtApp", ['ui.router', 'firebase']);

pdtApp.controller("LogInCtrl", function($scope, $state, $firebaseObject, $rootScope, AuthService) {
    var rootRef = new Firebase("https://pdttools.firebaseIO.com");
    $scope.groupPassword = $firebaseObject(rootRef.child("weakGroupPassword"));
    $scope.adminPassword = $firebaseObject(rootRef.child("weakAdminPassword"));

    $scope.logIn = function(password) {
        if (password == $scope.groupPassword.$value) {
            console.log("Group password correct");
            AuthService.logIn();
            $state.go('housePointView');
        } else if (password == $scope.adminPassword.$value) {
            console.log("Admin password correct");
        } else {
            console.log("Auth failed");
        }
    };
});

pdtApp.controller("housePointCtrl", function($scope, $rootScope) {
    $rootScope.$on('$stateChangeSuccess', function(event, toState, toParams, fromState, fromParams, options){
        if (toState.name == "housePointView") {
            console.log("House housePointView");
        }
    })

});


pdtApp.factory('AuthService', function() {
    var authService = {};
    authService.loggedIn = false;

    authService.logIn = function() {
        console.log("Logging in");
        authService.loggedIn = true;
    }

    authService.logOut = function() {
        console.log("Logging out");
        authService.loggedIn = false;
    }

    authService.isAuthenticated = function() {
        if (authService.loggedIn) {
            console.log("user IS logged in");
        } else {
            console.log("user IS NOT logged in");
        }
        return authService.loggedIn;
    }

    return authService;
});



pdtApp.config(function($stateProvider, $urlRouterProvider) {
    $stateProvider.state('logIn', {
        url: "/logIn",
        templateUrl: "partials/login.html",
        controller: "LogInCtrl",
        authenticate: false
    })


    $stateProvider.state('housePointView', {
        url: "/points",
        templateUrl: "partials/points.html",
        controller: 'housePointCtrl',
        authenticate: true
    })
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

