'use strict';

angular
    .module('quizApp')
    .config(config);

config.$inject = ['$routeProvider', '$locationProvider'];

function config($routeProvider, $locationProvider){
    $locationProvider.hashPrefix('!');
    $locationProvider.html5Mode(true);

    $routeProvider
    .when('/',{
        templateUrl: '/static/templates/homepage.html'
    })
    .when('/login',{
        templateUrl: '/static/templates/template.html',
        controller: 'LoginController',
        controllerAs: 'vm'
    })
    .when('/logout',{
        templateUrl: '/static/templates/template.html',
        controller: 'LogoutController',
        controllerAs: 'vm'
    })
    .when('/signup',{
        templateUrl: '/static/templates/template.html',
        controller: 'SignupController',
        controllerAs: 'vm'
    })
    .when('/quizzes',{
        templateUrl: '/static/templates/template.html',
        controller: 'QuizListController',
        controllerAs: 'vm'
    })
    .when('/quiz',{
        templateUrl: '/static/templates/template.html',
        controller: 'QuizFormController',
        controllerAs: 'vm'
    })
    .when('/results/:sessionid',{
        templateUrl: '/static/templates/template.html',
        controller: 'ResultsController',
        controllerAs: 'vm'
    });
}