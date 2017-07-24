(function(){

    'use strict';

    angular
        .module('quizApp')
        .controller('QuizListController', QuizListController);

    QuizListController.$inject = ['djangoUrl', '$cookies', '$location', 'Authentication'];

    function QuizListController(djangoUrl, $cookies, $location, Authentication) {
        var vm = this;

        if(!Authentication.isAuthenticated()){
            $location.url('/');
        }

        vm.content = djangoUrl.reverse('quiz:quiz_list');

        vm.start = function(quiz_id){
            $cookies.put('quizid', quiz_id.toString());
            $location.url('/quiz');
        }
    }

})();