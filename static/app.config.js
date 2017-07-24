(function () {
    'use strict';

    angular
        .module('quizApp')
        .config(config);

    config.$inject = ['$httpProvider', '$sceProvider'];

    function config($httpProvider, $sceProvider){
        // $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

        $sceProvider.enabled(true);

        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
})();