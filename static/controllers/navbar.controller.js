(function(){

    'use strict';

    angular
        .module('quizApp')
        .controller('NavbarController', NavbarController);

    NavbarController.$inject = ['Authentication', '$scope'];

    function NavbarController(Authentication, $scope) {
        var vm = this;

        $scope.$on('$locationChangeStart', function(event){
            vm.loggedin = Authentication.isAuthenticated();
        });

        vm.logout = function(){
            Authentication.logout();
        }
    }

})();