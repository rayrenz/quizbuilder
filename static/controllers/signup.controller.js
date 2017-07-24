(function(){

    'use strict';

    angular
        .module('quizApp')
        .controller('SignupController', SignupController);

    SignupController.$inject = ['$sce', '$http', 'djangoUrl'];

    function SignupController($sce, $http, djangoUrl) {
        var vm = this;

        $http.get(djangoUrl.reverse('quiz:signup'))
            .then(function successCallback(response){
                vm.content = $sce.trustAsHtml(response.data);
            }, function errorCallback(response){

            });
    }

})();