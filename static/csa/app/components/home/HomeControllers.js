    var HomeControllers = angular.module('HomeControllers');

    HomeControllers.$inject = ['$location', '$scope'];
    /*Register Controller
     */
    HomeControllers.controller('HomeController', function($scope, HomeServices) {
        $("#flipflip").hover(function() {
            $(this).toggleClass("animated flip")
        })
        $scope.home = function() {}

    });
