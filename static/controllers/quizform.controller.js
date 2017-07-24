(function(){

    'use strict';

    angular
        .module('quizApp')
        .controller('QuizFormController', QuizFormController);

    QuizFormController.$inject = ['djangoUrl', '$cookies', 'Authentication', '$location', '$http'];

    function QuizFormController(djangoUrl, $cookies, Authentication, $location, $http) {
        var vm = this;

        if(!Authentication.isAuthenticated()){
            $location.url('/');
        }
        if(!$cookies.get('quizid')){
            $location.url('/quizzes');
        }


        vm.content = djangoUrl.reverse('quiz:quiz_form', {'quiz_id': $cookies.get('quizid')});
        vm.count=0;
        vm.answers = {};

        vm.setAnswer = function (questionid, choiceid){
            vm.answers[questionid] = choiceid;
            vm.isfinished();
        };

        vm.isfinished = function(){
          return Object.keys(vm.answers).length === vm.count;
        };

        vm.submit = function(){
            console.log(vm.answers);
            $cookies.putObject('quizdata', JSON.stringify(vm.answers));
            console.log($cookies.getObject('quizdata'));
            $http.post(djangoUrl.reverse('quiz:check', {quiz_id: $cookies.get('quizid')}))
                .then(function successCallback(response){
                    $location.url('/results/' + response.data);
                });
        }
    }

})();