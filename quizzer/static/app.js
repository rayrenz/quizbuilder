var quizApp = angular.module('quizApp', ['ngRoute']);

quizApp.config(function($routeProvider){
    $routeProvider
        .when('/', {
            templateUrl: '/static/templates/welcome.html',
        })
        .when('/quizzes', {
            templateUrl: '/static/templates/quiz.html',
            controller: 'QuizController'
        })
        .when('/quiz/:quizid', {
            templateUrl: '/static/templates/quizform.html',
            controller: 'QuizFormController'
        })
        .when('/quiz/:quizid/:sessionid/results', {
            templateUrl: '/static/templates/resultsform.html',
            controller: 'ResultsFormController'
        })
        .when('/logout', {
            templateUrl: '/static/templates/logout.html',
            controller: 'LogoutController'
        })
        .when('/register', {
            templateUrl: '/static/templates/register.html',
            controller: 'RegisterController'
        })
        .when('/login', {
            templateUrl: '/static/templates/loginpage.html',
            controller: 'LoginController'
        });
});

quizApp.controller('ResultsFormController', function($scope, $http, $sce, $routeParams){
    $http({
        method: 'GET',
        url: '/quiz/' + $routeParams.quizid + '/' + $routeParams.sessionid + '/results'
    }).then(function successCallback(response){
            $scope.content = $sce.trustAsHtml(response.data);
        }, function errorCallback(response){
            console.error(response.statusText);
        });
});

quizApp.controller('QuizController', function($scope, $http, $sce){
    $http({
        method: 'GET',
        url: '/quizzes'
    }).then(function successCallback(response){
            $scope.content = $sce.trustAsHtml(response.data);
        }, function errorCallback(response){
            console.error(response.statusText);
        });
});

quizApp.controller('LogoutController', function($scope, $http, $location){
    $http({
        method: 'GET',
        url: '/logout'

    }).then(function successCallback(response){
            $location.path('/');
        }, function errorCallback(response){
            console.error(response.statusText);
        });
});

quizApp.controller('QuizFormController', function($scope, $http, $routeParams){
    $http({
        method: 'GET',
        url: '/api/quiz/' + $routeParams.quizid
    }).then(function successCallback(response){
            $scope.content = response.data;
            console.log(response.data)
        }, function errorCallback(response){
            console.error(response.statusCode);
        });

    $scope.submit = function() {
        console.log($scope);
        // $http({
        //     method: 'POST',
        //     url: '/quiz/' + scope.content.id
        //     data: {
        //
    }
});

quizApp.controller('LoginController', function($scope, $http, $sce){
    $scope.user = {};

    $scope.submit = function() {
        alert($('#id_username').val());
    };

    $http({
        method: 'GET',
        url: '/login'

    }).then(function successCallback(response){
            $scope.content = $sce.trustAsHtml(response.data);
        }, function errorCallback(response){
            console.error(response.statusText);
        });


});

quizApp.controller('RegisterController', function ($scope, $http, $sce) {
    $http({
        method: 'GET',
        url: '/register'

    }).then(function successCallback(response){
            $scope.content = $sce.trustAsHtml(response.data);
        }, function errorCallback(response){
            console.error(response.statusText);
        });
});