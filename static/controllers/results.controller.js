(function(){

    'use strict';

    angular
        .module('quizApp')
        .controller('ResultsController', ResultsController);

    ResultsController.$inject = ['djangoUrl', '$cookies', 'Authentication', '$location', '$routeParams', '$scope'];

    function ResultsController(djangoUrl, $cookies, Authentication, $location, $routeParams, $scope) {
        var vm = this;
        if(!Authentication.isAuthenticated()){
            $location.url('/');
        }
        $scope.$routeParams = $routeParams;
        vm.content = djangoUrl.reverse('quiz:quiz_results', {session_id: $routeParams.sessionid});
    }

})();