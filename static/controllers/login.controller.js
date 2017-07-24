(function(){

    'use strict';

    angular
        .module('quizApp')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['djangoUrl', 'Authentication'];

    function LoginController(djangoUrl, Authentication) {
        var vm = this;

        vm.content = djangoUrl.reverse('quiz:login_get');

        vm.submit = function(){
            Authentication.login(vm.username, vm.password);
        };
    }

})();