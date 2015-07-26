    var EmployeesManagerControllers = angular.module('EmployeesManagerControllers');

    EmployeesManagerControllers.$inject = ['$location', '$scope', ];
    /*Register Controller
     */
    EmployeesManagerControllers.controller('EmployeesManagerController', function($scope, $http,$q, EmployeesManagerServices) {
            
                init = function() {
                $scope.TEAM_NAME   = 'ProLookApp Team';
                $scope.Employees_URL = 'www.prolookapp.com';
                $scope.Employees_EMAIL = 'm_mokhtari@esi.dz';
                $scope.Employees_DOMAIN = 'Ecommerce';
                $scope.Employees_LOCATION = 'Algeria';
                $scope.Employees_DESC = 'Task manager';


                }

    
                init();
            
                $scope.updateTeamName = function(data) {
                    var d = $q.defer();
                    $http.post('/api/accounts/Employees/email', {
                        value: data
                    }).success(function(res) {
                        res = res || {};
                        if (res.status === 'ok') { // {status: "ok"}
                            d.resolve()
                        } else { // {status: "error", msg: "Username should be `awesome`!"}
                            /*d.resolve(res.msg)*/
                            /*d.resolve("billing email exist")*/
                            d.resolve()
                        }
                    }).error(function(e) {
                        d.reject('Server error!');
                    });
                    return d.promise;
                }
                });
