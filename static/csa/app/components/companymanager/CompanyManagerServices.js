angular.module('CompanyManagerControllers').factory('CompanyManagerServices', ['$http',
    function($http) {
        /**
         * @name HomeService
         * @desc The Factory to be returned
         */
        var CompanyManagerServices = {};
        /**
         * @name home
         * @desc Try to set the home page
         * @param {string} username The username entered by the user
         * @param {string} password The password entered by the user
         * @param {string} email The email entered by the user
         * @returns {Promise}
         */
        CompanyManagerServices.updatename = function () {
            return $http.post('/api/company').success(function(data) {
                console.log("updatename data is back ");
            }).error(function() {
                console.log('no response factorym server ');
            });
        }
    return CompanyManagerServices;
    }
]);