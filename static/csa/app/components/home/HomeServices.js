angular.module('HomeControllers').factory('HomeServices', ['$http',
    function($http) {
        /**
         * @name HomeService
         * @desc The Factory to be returned
         */
        var HomeServices = {};
        /**
         * @name home
         * @desc Try to set the home page
         * @param {string} username The username entered by the user
         * @param {string} password The password entered by the user
         * @param {string} email The email entered by the user
         * @returns {Promise}
         */
        HomeServices.home = function home() {
            return $http.post('/').success(function(data) {
                
                console.log("home data is back ");
            }).error(function() {
                console.log('no response from home ');
            });
        }
    return HomeServices;
    }
]);