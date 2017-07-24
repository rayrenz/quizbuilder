(function(){

    'use strict';

    angular
        .module('authentication.services')
        .factory('Authentication', Authentication);

    Authentication.$inject = ['djangoUrl', '$http', '$cookies', '$location'];

    function Authentication(djangoUrl, $http, $cookies, $location) {
        var Authentication = {
            login: login,
            setAuthenticated: setAuthenticated,
            isAuthenticated: isAuthenticated,
            logout: logout,
            unauthenticate: unauthenticate,
            getAuthenticated: getAuthenticated,
        };

        return Authentication;

        function login(username, password){
            var data = {
                username: username,
                password: password
            };

            $http.post(djangoUrl.reverse('quiz:login_post', data))
                .then(function successCallback(response){
                    Authentication.setAuthenticated(response.data);
                    $location.url('/quizzes');
                }, function errorCallback(response){
                    console.error(response.status);
                });
        }

        function setAuthenticated(account){
            $cookies.put('user', JSON.stringify(account));
        }
        
        function isAuthenticated(){
            return !!$cookies.get('user');
        }

        function unauthenticate(){
            delete $cookies.remove('user');
        }

        function logout(){
            $http.post(djangoUrl.reverse('quiz:logout'))
                .then(function successCallback(response){
                    Authentication.unauthenticate();
                    $location.url('/');
                }, function errorCallback(response){
                    console.error('Error occurred upon logging out!');
                });
        }

        function getAuthenticated(){
            if(!$cookies.authenticatedAccount){
                return;
            }
            return JSON.parse($cookies.authenticatedAccount);
        }

    }

})();