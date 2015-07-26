    var CompanyManagerControllers = angular.module('CompanyManagerControllers');

    CompanyManagerControllers.$inject = ['$location', '$scope', ];
    /*Register Controller
     */
    CompanyManagerControllers.controller('CompanyManagerController', function($scope, $http,$q, CompanyManagerServices) {
                $scope.COMPANY_NAME = 'ProLookApp';
                $scope.COMPANY_URL = 'www.prolookapp.com';
                $scope.COMPANY_EMAIL = 'm_mokhtari@esi.dz';
                $scope.COMPANY_DOMAIN = 'Ecommerce';
                $scope.COMPANY_LOCATION = 'Algeria';
                $scope.COMPANY_DESC = 'Task manager';
                init = function() {


                    $scope.COMPANY_NAME_ = 'LG';
                    $scope.COMPANY_DOMAIN_ = 'Tech';
                    $scope.company_info_show = true;
                    $scope.mile_stones_show = false;
                    $scope.billing_info_show = false;
                    $("#companyinfo").toggleClass("menuboxclick", true);

                    $scope.billingemail_editing_show = false;
                    //get page scope variables

                }

    
                init();
                $scope.company_info_click = function() {
                    $scope.company_info_show = true;
                    $scope.mile_stones_show = false;
                    $scope.billing_info_show = false;
                    $("#companyinfo").toggleClass("menuboxclick", true);
                    $("#milestones").removeClass("menuboxclick");
                    $("#billinginfo").removeClass("menuboxclick");

                };
                $scope.mile_stones_click = function() {
                    $scope.company_info_show = false;
                    $scope.mile_stones_show = true;
                    $scope.billing_info_show = false;
                    $("#companyinfo").removeClass("menuboxclick");
                    $("#milestones").toggleClass("menuboxclick", true);
                    $("#billinginfo").removeClass("menuboxclick");
                };
                $scope.billing_info_click = function() {
                    $scope.company_info_show = false;
                    $scope.mile_stones_show = false;
                    $scope.billing_info_show = true;
                    $("#companyinfo").removeClass("menuboxclick");
                    $("#milestones").removeClass("menuboxclick");
                    $("#billinginfo").toggleClass("menuboxclick", true);

                    setTimeout(function() {
                        $("#billingemail").focus();
                    }, 500);
                };
                $scope.billingemail_click = function() {

                    $scope.billingemail_editing_show = true;

                    setTimeout(function() {
                        $scope.billingemail_editing_show = false;
                        $scope.$apply();
                    }, 800);
                };
                $scope.updateBillingEmail = function(data) {
                    var d = $q.defer();
                    $http.post('/api/accounts/', {
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
