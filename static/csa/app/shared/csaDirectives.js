
var csaDirectives = angular.module('csaDirectives');

csaDirectives.directive('protextfield', function($timeout, $http) {
    return {
        restrict: 'AE',
        replace: true,
        scope: {
            URL: '@prourl',
            PLACEH: '@plch',
        }, //isolated scope
        templateUrl: "/static/csa/app/shared/partials/protextfield.html",
        link: function(scope, elem, attrs) {
            elem.find('i').hide()
            elem.find('input').val();
            console.log(attrs['ngModel'])

            scope.submit = function($event) {
                elem.find('i').show()


                //send to server
                console.log('sending to ' + scope.prourl)
                text = elem.find('input').val();
                console.log(text);
                if (text == '') {
                    scope.NAME = scope.NAME;
                    elem.find('i').hide()
                } else {
                    //send to sevrer
                    var data = [scope.editvar];
                    server = $http.post(scope.URL).success(function(data) {
                        console.log("Update value " + scope.editvar + " to URL" + scope.URL + " is Done");
                    }).error(function() {
                        console.log("Update value " + scope.editvar + " to URL" + scope.URL + " is ERROR");
                    });


                    if (server) {
                        scope.NAME = text;
                    } else {
                        console.log('Show Error Message');
                    }
                    setTimeout(function() {
                        // body...
                        elem.find('i').hide();
                    }, 1000)
                    console.log(scope.NAME)
                }

            }
            scope.changing = function() {
                //update the width of the input
                /* var len = $("input#input1").textWidth(scope.editvar); //get the new size of the input
                 if (len > 20) {
                     $("input#input1").width(len);
                 }*/
            }
            scope.lostfocus = function() {
                /* console.log('lostfocus')
                 scope.editvar = scope.NAME;
                 var len = $("input#input1").textWidth(scope.editvar); //get the new size of the input
                 $("input#input1").width(len);
                 $("input#input1").val(scope.editvar);
                 scope.showEdit = false;*/
            }
        }
    };
});

csaDirectives.directive('editinplace', function($timeout, $http) {
    return {
        restrict: 'AE',
        replace: true,
        scope: {
            URL: '@dirurl',
            NAME: '@dirvar',
        }, //isolated scope
        templateUrl: "/static/csa/app/shared/partials/editinplace.html",
        link: function(scope, elem, attrs) {
            scope.editvar = scope.NAME;
            scope.showEdit = false;

            $("input#input1").width($("input#input1").textWidth(scope.editvar));
            scope.textclick = function(value) {

                scope.showEdit = true;
                setTimeout(function() {
                    $("input#input1").focus();
                }, 10);
            }
            scope.submit = function($event) {
                // hide the edit field
                scope.showEdit = false;
                // submit form
                //send to server
                console.log('sending to ' + scope.URL)
                if (scope.editvar == '') {
                    scope.editvar = scope.NAME;
                } else {
                    //send to sevrer
                    var data = [scope.editvar];
                    server = $http.post(scope.URL).success(function(data) {
                        console.log("Update value " + scope.editvar + " to URL" + scope.URL + " is Done");
                    }).error(function() {
                        console.log("Update value " + scope.editvar + " to URL" + scope.URL + " is ERROR");
                    });


                    if (server) {
                        scope.NAME = scope.editvar;
                    } else {
                        console.log('Show Error Message');
                    }

                }

            }
            scope.changing = function() {
                //update the width of the input
                var len = $("input#input1").textWidth(scope.editvar); //get the new size of the input
                if (len > 20) {
                    $("input#input1").width(len);
                }
            }
            scope.lostfocus = function() {
                console.log('lostfocus')
                scope.editvar = scope.NAME;
                var len = $("input#input1").textWidth(scope.editvar); //get the new size of the input
                $("input#input1").width(len);
                $("input#input1").val(scope.editvar);
                scope.showEdit = false;
            }
        }
    };
});

csaDirectives.directive('dhxScheduler', function() {
    return {
        restrict: 'A',
        scope: true,
        transclude: true,
        template: '<div class="dhx_cal_navline" ng-transclude></div><div class="dhx_cal_header"></div><div class="dhx_cal_data"></div>',



        link: function($scope, $element, $attrs, $controller) {
            //default state of the scheduler
            if (!$scope.scheduler)
                $scope.scheduler = {};
            $scope.scheduler.mode = $scope.scheduler.mode || "month";
            $scope.scheduler.date = $scope.scheduler.date || new Date();

            //watch data collection, reload on changes
            $scope.$watch($attrs.data, function(collection) {
                scheduler.clearAll();
                scheduler.parse(collection, "json");
            }, true);

            //mode or date
            $scope.$watch(function() {
                return $scope.scheduler.mode + $scope.scheduler.date.toString();
            }, function(nv, ov) {
                var mode = scheduler.getState();
                if (nv.date != mode.date || nv.mode != mode.mode)
                    scheduler.setCurrentView($scope.scheduler.date, $scope.scheduler.mode);
            }, true);

            //size of scheduler
            $scope.$watch(function() {
                return $element[0].offsetWidth + "." + $element[0].offsetHeight;
            }, function() {
                scheduler.setCurrentView();
            });

            //styling for dhtmlx scheduler
            $element.addClass("dhx_cal_container");

            //init scheduler
            scheduler.init($element[0], $scope.scheduler.mode);
        }
    }
});
/*csaDirectives.directive('dhxTemplate', ['$filter', function($filter) {
    scheduler.aFilter = $filter;

    return {
        restrict: 'AE',
        terminal: true,

        link: function($scope, $element, $attrs, $controller) {
            $element[0].style.display = 'none';

            var template = $element[0].innerHTML;
            template = template.replace(/[\r\n]/g, "").replace(/"/g, "\\\"").replace(/\{\{event\.([^\}]+)\}\}/g, function(match, prop) {
                if (prop.indexOf("|") != -1) {
                    var parts = prop.split("|");
                    return "\"+scheduler.aFilter('" + (parts[1]).trim() + "')(event." + (parts[0]).trim() + ")+\"";
                }
                return '"+event.' + prop + '+"';
            });
            var templateFunc = Function('sd', 'ed', 'event', 'return "' + template + '"');
            scheduler.templates[$attrs.dhxTemplate] = templateFunc;
        }
    };
}]);*/
