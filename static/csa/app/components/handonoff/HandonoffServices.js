/**
 *@name HandonoffServices
 *@desc Handonoff module services
 */
angular.module('HandonoffControllers').factory('HandonoffServices', ['$http','$location',
    function($http,$location) {
        /**
         * @name HandonoffService
         * @desc The Factory to be returned
         */
        var HandonoffServices = {};
        var newname = 'old';
        var response;
        /**
         * @name register
         * @desc Try to register a new user
         * @param {string} username The username entered by the user
         * @param {string} password The password entered by the user
         * @param {string} email The email entered by the user
         * @returns {Promise}
         */
        HandonoffServices.register = function register(email,username,password) {
            return $http.post('../api/accounts/', {
                username: username,
                password: password,
                email: email
            }).success(function(promise) {
               if(promise.status == 'VALID_INFO'){
                    window.location = '/WorkPlace/';
                }
            }).error(function() {
                console.log('no response from register ');
            });
        }
        /**
         * @name signin
         * @desc Try to signin a  user
         * @param {string} username The username entered by the user
         * @param {string} password The password entered by the user
         * @param {string} email The email entered by the user
         * @returns {Promise}
         */
        HandonoffServices.signin = function signin(username,password) {
            return $http.post('/login/', {
                username: username,
                password: password
            }).success(function(data) {
                if(data.status =='OK_LOGIN'){
                    window.location = '/WorkPlace/';
                }else{

                }
                
            }).error(function() {
                console.log('no response from signin ');
            });
        }
        /**
         * @name signout
         * @desc Try to signout a  user
         * @param {string} username The username entered by the user
         * @param {string} password The password entered by the user
         * @param {string} email The email entered by the user
         * @returns {Promise}
         */
        HandonoffServices.signout = function signout(email, password, username) {
            return $http.post('/logout/');
        }
        return HandonoffServices;
    }
]);