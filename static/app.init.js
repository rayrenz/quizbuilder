(function () {
    'use strict';

    angular
        .module('quizApp')
        .run(run);

    run.$inject = ['$http', '$sceProvider', '$cookies', '$httpProvider'];

    function run($http, $sceProvider, $cookies, $httpProvider){
        // $sceProvider.enabled(true);
        // // $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        // // $cookies.defaults.xsrfCookieName = 'csrftoken';
        // //
        // //
        // // $httpProvider.defaults.headers.common['X-CSRFToken'] = '{{ csrf_token }}';
        // // $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    }
})();