    var WorkplaceControllers = angular.module('WorkplaceControllers');

    WorkplaceControllers.$inject = ['$location', '$scope', ];
    /*Register Controller
     */
    WorkplaceControllers.controller('WorkplaceController', function($scope, WorkplaceServices) {

        init = function() {

            //get page scope variables
            $scope.COMPANY_NAME = 'ProLookApp';
        }
        init();
        $scope.companymanagerclick = function() {
            console.log("CLICK");
            //$("#companymanager").toggleClass("animated flip");
            $("#handovermanager").toggleClass("animated bounceOut");
            $("#taskmanager").toggleClass("animated bounceOut");
            $("#employeesmanager").toggleClass("animated bounceOut");
            $("#kmmanager").toggleClass("animated bounceOut");
            setTimeout(function() {
                window.location = "/WorkPlace/CompanyManager/";
            }, 800);
        };
        $scope.handovermanagerclick = function() {
            console.log("CLICK");
            //window.location = "/WorkPlace/CompanyManager/";
            //$("#handovermanager").toggleClass("animated flip");
            // $("#companymanager").toggleClass("animated pulse");
            $("#companymanager").toggleClass("animated bounceOut");
            $("#taskmanager").toggleClass("animated bounceOut");
            $("#employeesmanager").toggleClass("animated bounceOut");
            $("#kmmanager").toggleClass("animated bounceOut");
            setTimeout(function() {
                window.location = "/WorkPlace/HandOverManager/";
            }, 800);
        };
        $scope.taskmanagerclick = function() {
            console.log("CLICK");
            //window.location = "/WorkPlace/CompanyManager/";
            //$("#taskmanager").toggleClass("animated flip");
            $("#companymanager").toggleClass("animated bounceOut");
            $("#handovermanager").toggleClass("animated bounceOut");
            $("#employeesmanager").toggleClass("animated bounceOut");
            $("#kmmanager").toggleClass("animated bounceOut");
            setTimeout(function() {
                window.location = "/WorkPlace/TaskManager/";
            }, 800);
        };
        $scope.employeesmanagerclick = function() {
            console.log("CLICK");
            //window.location = "/WorkPlace/CompanyManager/";
            //$("#employeesmanager").toggleClass("animated flip");
            $("#companymanager").toggleClass("animated bounceOut");
            $("#handovermanager").toggleClass("animated bounceOut");
            $("#taskmanager").toggleClass("animated bounceOut");
            $("#kmmanager").toggleClass("animated bounceOut");
            setTimeout(function() {
                window.location = "/WorkPlace/EmployeesManager/";
            }, 800);
        };
        $scope.kmmanagerclick = function() {
            console.log("CLICK");
            //window.location = "/WorkPlace/CompanyManager/";
            //$("#kmmanager").toggleClass("animated flip");
            $("#companymanager").toggleClass("animated bounceOut");
            $("#handovermanager").toggleClass("animated bounceOut");
            $("#taskmanager").toggleClass("animated bounceOut");
            $("#employeesmanager").toggleClass("animated bounceOut");
            setTimeout(function() {
                window.location = "/WorkPlace/KMManager/";
            }, 800);
        };


    });
    WorkplaceControllers.controller('WorkplaceHeaderController', function($scope, WorkplaceServices) {
        $scope.COMPANY_NAME_URL = '/api/accounts/';
        init = function() {
            $scope.COMPANY_NAME = 'ProLookApp';
            setTimeout(function () {
                console.log("This is me the WorkplaceHeaderController from WorkPlace");
            },3000);
        };
        init();
        $scope.home_click = function  () {
            window.location = "/WorkPlace/";
        }
    });
