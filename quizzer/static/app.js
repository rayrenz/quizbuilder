var quizApp = angular.module('quizApp', ['ngRoute']);

quizApp.config(function($routeProvider){
    $routeProvider
        .when('/', {
            templateUrl: '/static/templates/welcome.html',
        })
        .when('/quizzes', {
            templateUrl: '/static/templates/template.html',
            controller: 'QuizController',
            controllerAs: 'vm'
        })
        .when('/quiz/:quizid', {
            templateUrl: '/static/templates/template.html',
            controller: 'QuizFormController',
            controllerAs: 'vm'
        })
        .when('/quiz/:quizid/:sessionid/results', {
            templateUrl: '/static/templates/template.html',
            controller: 'ResultsFormController',
            controllerAs: 'vm'
        })
        .when('/logout', {
            templateUrl: '/static/templates/template.html',
            controller: 'LogoutController',
            controllerAs: 'vm'
        })
        .when('/register', {
            templateUrl: '/static/templates/template.html',
            controller: 'RegisterController',
            controllerAs: 'vm'
        })
        .when('/login', {
            templateUrl: '/static/templates/template.html',
            controller: 'LoginController',
            controllerAs: 'vm'
        });
});

quizApp.controller('ResultsFormController', function($scope, $http, $sce, $routeParams){
    var vm = this;

    $http({
        method: 'GET',
        url: '/quiz/' + $routeParams.quizid + '/' + $routeParams.sessionid + '/results'
    }).then(function successCallback(response){
            vm.content = $sce.trustAsHtml(response.data);
        }, function errorCallback(response){
            console.error(response.statusText);
        });
});

quizApp.controller('QuizController', function($scope, $http, $sce){
    var vm = this;

    $http({
        method: 'GET',
        url: '/quizzes'
    }).then(function successCallback(response){
            vm.content = $sce.trustAsHtml(response.data);
        }, function errorCallback(response){
            console.error(response.statusText);
        });
});

quizApp.controller('LogoutController', function($scope, $http, $location){
    $http({
        method: 'GET',
        url: '/logout'

    }).then(function successCallback(response){
            window.location = '/';
        }, function errorCallback(response){
            console.error(response.statusText);
        });
});

quizApp.controller('QuizFormController', function($scope, $sce, $http, $routeParams){
    var vm = this;

    $http({
        method: 'GET',
        url: '/quiz/' + $routeParams.quizid + '/'
    }).then(function successCallback(response){
            vm.content = $sce.trustAsHtml(response.data);
            console.log(response.data)
        }, function errorCallback(response){
            console.error(response.statusText);
        });
});

quizApp.controller('LoginController', function($scope, $http, $sce){
  var vm = this;

  $http({
    method: 'GET',
    url: '/login'

  }).then(function successCallback(response){
      vm.content = $sce.trustAsHtml(response.data);
    }, function errorCallback(response){
      console.error(response.statusText);
    });

  vm.submit = function(){
    alert(vm.username + vm.password + '!');
  }

});

quizApp.controller('RegisterController', function ($scope, $http, $sce) {
    var vm = this;

    $http({
        method: 'GET',
        url: '/register'

    }).then(function successCallback(response){
            vm.content = $sce.trustAsHtml(response.data);
        }, function errorCallback(response){
            console.error(response.statusText);
        });
});